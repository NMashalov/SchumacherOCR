

from transformers import DetrConfig, AutoModelForObjectDetection
from transformers import AutoFeatureExtractor


class YoloSettings:
    repo="NMashalov/PhysicsYoLO"



class YoloDetector:
    def __init__(self):
        self.model = AutoModelForObjectDetection.from_pretrained(YoloSettings.repo,num_labels=2,)
    
        self.feature_extractor = AutoFeatureExtractor.from_pretrained("hustvl/yolos-small", size=512, max_size=864)

    def infer(self):
        encoding = self.feature_extractor(images=img, annotations=target, return_tensors="pt")