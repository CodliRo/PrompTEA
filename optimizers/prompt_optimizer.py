import torch
from models.gpt2_model import GPT2Model
from utils.prompt_utils import load_templates, generate_variations
from utils.evaluation_utils import neural_evaluation
from config import Config

class PromptOptimizer:
    def __init__(self):
        self.model = GPT2Model()
        self.templates = load_templates(Config.TEMPLATES_FILE)

    def optimize_prompt(self, original_prompt):
        current_prompt = original_prompt
        history = [(current_prompt, self.model.evaluate(current_prompt))]

        for _ in range(Config.MAX_ITERATIONS):
            variations = generate_variations(current_prompt, self.templates, Config.NUM_VARIATIONS)
            evaluated = neural_evaluation(variations, self.model)
            best_prompt, neural_score = evaluated[0]
            if neural_score > history[-1][1]:
                current_prompt = best_prompt
                history.append((current_prompt, neural_score))

        return {
            'original': original_prompt,
            'optimized': history[-1][0],
            'score_improvement': history[-1][1] - history[0][1],
            'history': history
        }