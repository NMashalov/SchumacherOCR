from tqdm import tqdm
import pypdf
from pathlib import Path

class PdfText:
    def __init__(self, path: Path):
        reader = pypdf.PdfReader(path)
        output = [page.extract_text() for page in tqdm(reader.pages)]