import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class GPT2Model:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def evaluate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model(**inputs)
        score = torch.softmax(outputs.logits[0], dim=-1).max().item()
        return score