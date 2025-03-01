from optimizers.prompt_optimizer import PromptOptimizer
def main():
    optimizer = PromptOptimizer()
    original_prompt = "Tell me about ChatGPT"
    result = optimizer.optimize_prompt(original_prompt)

    print(f"Original Prompt: {result['original']}")
    print(f"Original Score: {result['history'][0][1]:.3f}")
    print(f"Optimized Prompt: {result['optimized']}")
    print(f"Final Score: {result['history'][-1][1]:.3f}")
    print(f"Score Improvement: {result['score_improvement']:.3f}")

    print("\nOptimization History:")
    for prompt, score in result['history']:
        print(f"Score: {score:.3f} - {prompt}")

if __name__ == "__main__":
    main()