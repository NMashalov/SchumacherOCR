from datasets import load_dataset
from datasets import Image
load_dataset("imagefolder", data_dir="books/").cast_column('image', Image(decode=False)).add_column('ocr',output)



def diploma():


    