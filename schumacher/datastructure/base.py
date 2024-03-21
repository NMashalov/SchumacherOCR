from dataclasses import dataclass
from pathlib import Path

@dataclass
class Case:
    text: str
    hash: str
    illustration: list[str]
    answer: str 
    solution: str



def merge_json(dir: Path):
    pass