from datasets import load_dataset, Image

'''
Images are hold as binary strings for speed of processing
'''


def get_ocr_dataset():
    return load_dataset("NMashalov/ru_book_datasets").cast_column('image', Image(decode=False))

def get_image_dataset():
    return load_dataset("NMashalov/task_illustrations_dataset").cast_column('image', Image(decode=False))['train']['image']