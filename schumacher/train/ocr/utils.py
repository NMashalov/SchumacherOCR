def train_tokenizer(self):
    split = (split for text in self.train_dataset for split in text['ocr'].split('\n') if len(split)>0)
    self.processor.tokenizer = self.processor.tokenizer.train_new_from_iterator(train_text, 20_000)
