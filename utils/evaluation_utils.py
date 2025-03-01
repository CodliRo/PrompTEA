def neural_evaluation(prompts, model):
    results = []
    for prompt in prompts:
        score = model.evaluate(prompt)
        results.append((prompt, score))
    return sorted(results, key=lambda x: x[1], reverse=True)