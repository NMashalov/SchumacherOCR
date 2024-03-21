from pathlib import Path
import pypdfium2
from tqdm import tqdm
import subprocess 
import io
import typing as tp
import base64
from .image import ImgProcessor

class GhostScriptProcessor:
    def to_folder(self):
        try:
            subprocess.Popen(
            "mkdir -p /content/books/{} && gs -r300 -dNOPAUSE -dBATCH -sDEVICE=png16m -sOutputFile='/content/books/{}/Pic-%d.png' {}.pdf"
            )
        except Exception as e:
            print('execute sudo apt-get install ghostscript')


class DjvuMixin:

    def to_pdf(self):
        #djvulibre-bin 
        try:
            subprocess.Popen(
            "mkdir -p /content/books/{} && gs -r300 -dNOPAUSE -dBATCH -sDEVICE=png16m -sOutputFile='/content/books/{}/Pic-%d.png' {}.pdf"
            )
        except Exception as e:
            print('Please execute: sudo apt-get install ghostscript')
        

class PdfProcessor:
    def __init__(self, pdf_path: Path, dpi: int =96):
        self.pdf = pypdfium2.PdfDocument(pdf_path)
        self.dpi = dpi

    def stream(self, dpi = 96):
        return self.pdf.render(
            pypdfium2.PdfBitmap.to_pil,
            scale=self.dpi / 72,
        )       
        
    def to_image_folder(self,output_folder: Path):
        output_folder.mkdir(exist_ok=True)

        for i,image in tqdm(enumerate(self.stream)):
            image.save(output_folder / f"{i:03d}.png", "png")
        

    
                   




   

