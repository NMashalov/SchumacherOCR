import pytest
from pathlib import Path


@pytest.fixture
def return_pdf_path_and_config():
    base_link = Path(__file__).parent / 'books'
    return {
        'config': base_link / 'config.yaml',
        'book': base_link / 'Perelman.pdf'
    }