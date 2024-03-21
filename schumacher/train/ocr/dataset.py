from torch.utils.data import Dataset
from PIL import Image
from tqdm import tqdm
import io
from datasets import Dataset
from transformers.models.nougat.processing_nougat import NougatProcessor


class OCRDataset(Dataset):
    def __init__(self,processor : NougatProcessor,dataset: Dataset):
        self.train_dataset = dataset['train']
        self.processor = processor

        self.train_tokenizer()

        self.images = self.process_images()
        self.text= self.process_text()
    
    def train_tokenizer(self):
        train_text: list[str]= self.train_dataset['ocr']
        split = (split for text in train_text for split in text.split('\n') if len(split)>0)
        tokenizer = self.processor.tokenizer.train_new_from_iterator(train_text, 20_000)
        self.processor.tokenizer = tokenizer

    def process_text(self):
        return self.processor.tokenizer.batch_encode_plus(self.train_dataset['ocr'])

    def process_images(self):
        return [self.processor.image_processor(row['page'],return_tensors="pt").pixel_values for row in tqdm(self.train_dataset)]     

    def __len__(self):
        return len(self.prepared_text)

    def __getitem__(self, idx):
        return self.images[idx], self.text[idx]