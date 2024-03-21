from enum import Enum
from PIL.Image import Image
# Load model directly
from transformers import AutoTokenizer, AutoModel
import torch

class NougatRepo(str,Enum):
    link="NMashalov/RuNougat"


class NougatOCr:
    def __init__(self,device='cuda'):
        self.processor = AutoTokenizer.from_pretrained(NougatRepo.link)
        self.model = AutoModel.from_pretrained(NougatRepo.link)
        self.device =device

    def process(self,image: list[Image]):
        self.processor


    def infer(self,pixel_values: torch.Tensor):
        outputs = self.model.generate(pixel_values.to(self.device),
            min_length=1,
            max_length=3584,
            bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
            return_dict_in_generate=True,
            output_scores=True,
            stopping_criteria=StoppingCriteriaList([StoppingCriteriaScores()]),
        )


        
        generated = self.processor.batch_decode(outputs[0], skip_special_tokens=True)[0]
        generated = self.processor.post_process_generation(generated, fix_markdown=False)
        print(generated)


from transformers import StoppingCriteria, StoppingCriteriaList
from collections import defaultdict

class RunningVarTorch:
    def __init__(self, L=15, norm=False):
        self.values = None
        self.L = L
        self.norm = norm

    def push(self, x: torch.Tensor):
        assert x.dim() == 1
        if self.values is None:
            self.values = x[:, None]
        elif self.values.shape[1] < self.L:
            self.values = torch.cat((self.values, x[:, None]), 1)
        else:
            self.values = torch.cat((self.values[:, 1:], x[:, None]), 1)

    def variance(self):
        if self.values is None:
            return
        if self.norm:
            return torch.var(self.values, 1) / self.values.shape[1]
        else:
            return torch.var(self.values, 1)


class StoppingCriteriaScores(StoppingCriteria):
    def __init__(self, threshold: float = 0.015, window_size: int = 200):
        super().__init__()
        self.threshold = threshold
        self.vars = RunningVarTorch(norm=True)
        self.varvars = RunningVarTorch(L=window_size)
        self.stop_inds = defaultdict(int)
        self.stopped = defaultdict(bool)
        self.size = 0
        self.window_size = window_size

    @torch.no_grad()
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor):
        last_scores = scores[-1]
        self.vars.push(last_scores.max(1)[0].float().cpu())
        self.varvars.push(self.vars.variance())
        self.size += 1
        if self.size < self.window_size:
            return False

        varvar = self.varvars.variance()
        for b in range(len(last_scores)):
            if varvar[b] < self.threshold:
                if self.stop_inds[b] > 0 and not self.stopped[b]:
                    self.stopped[b] = self.stop_inds[b] >= self.size
                else:
                    self.stop_inds[b] = int(
                        min(max(self.size, 1) * 1.15 + 150 + self.window_size, 4095)
                    )
            else:
                self.stop_inds[b] = 0
                self.stopped[b] = False
            return all(self.stopped.values()) and len(self.stopped) > 0