from dataclasses import dataclass
from pydantic import BaseModel
from enum import Enum
from pathlib import Path
import typing as tp
from schumacher.utils.processor import PdfProcessor, ImgProcessor
from datasketch import MinHash

@dataclass
class Image:
    base_64: str
    annotation: tp.Optional[str]
    minhash: str

@dataclass
class Page:
    number: int 
    minhash: str
    scan_base_64: str
    images: tp.Optional[list[Image]]
    text:str
    processor_name: str 

@dataclass
class Reference:
    authors: list[str]
    title: str

@dataclass
class Book:
    reference: Reference

class TextProcessorType(str,Enum):
    tesseract='tesseract'
    nougat='nougat'

class CVProcessorType(str,Enum):
    opencv='opencv'
    yolo='yolo'

class Reference(BaseModel):
    title: str
    authors: list[str]
    extra: dict[str]

class Options(BaseModel):
    image_folder: bool
    text_processor: TextProcessorType 

class Settings(BaseModel):
    path: Path
    reference: Reference
    options: Options

def get_text_model(name: tp.Optional[TextProcessorType]):
    pass

def get_illustration_model(name: tp.Optional[CVProcessorType]):
    pass

class DocFormatter:
    def __init__(self, config: Settings):
        self.config = config
        self.text_model = get_text_model()
        self.illust_model = get_illustration_model()  

    def load_doc(self):
        for page in PdfProcessor(self.config.path,output_folder='output'):
            ImgProcessor.fr

    def to_json(self,):
        