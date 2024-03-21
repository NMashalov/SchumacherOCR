import typer
from pathlib import Path
from enum import Enum
import os
import logging
from getpass import getpass
import typing as tp

from schumacher.processor import PdfProcessor


main =  typer.Typer()

class OcrModels(str,Enum):
    tesseract='tesseract'
    nougat='nougat'
    ru_nougat='ru-nougat'

class OCROutputType(str,Enum):
    json='json'
    markdown='md'


@main.command('ocr')
def pdf_to_img_folder(pdf_path: list[Path], preset_path: Path, model: OcrModels, output_type :OCROutputType):
    pass


utils =  typer.Typer()

@utils.command('images')
def yolo_process():
    pass


@main.command('img-folder')
def pdf_to_img_folder(pdf_paths: list[Path]):
    for path in pdf_paths:
        p = PdfProcessor(path)
        p.to_folder(path.parent / path.stem)

@main.command('mathpix')
def mathpix_processor(pdf_path: Path, matpix_token: tp.Optional[str] = None):
    pass

@main.command('arxiv-papers')
def arxiv_papers(pdf_paths: list[Path]):
    pass

pipeline =  typer.Typer()

@pipeline.command('images')
def yolo_process():
    pass


main.add_typer(extract,name='extract')

main()