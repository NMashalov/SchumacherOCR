from transformers import NougatProcessor, VisionEncoderDecoderModel
import torch
from enum import Enum

class Settings(str,Enum):
    base_model="facebook/nougat-base"


class NoughatProcessor:
    def __init__(self):
        processor = NougatProcessor.from_pretrained(Settings.base_model)
        model = VisionEncoderDecoderModel.from_pretrained(Settings.base_model)

    def train(self):
        pixel_values = self.processor(image, return_tensors="pt").pixel_values
        loss = self.model(pixel_values=pixel_values, labels=labels).loss