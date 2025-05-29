# PrompTEA: A Prompt Optimization Framework for Language Models (v1.1.2)

## Overview

**PrompTEA** is an open-source framework designed to optimize prompts for language models. The framework uses a combination of natural language processing (NLP) and machine learning techniques to generate high-quality prompts that elicit specific responses from language models. By providing a powerful and customizable tool for prompt engineering, PrompTEA helps users improve the performance of language models across a wide variety of tasks.

## Features

- **Prompt Optimization**: PrompTEA uses a novel optimization algorithm to generate prompts tailored to a specific language model and task.
- **Language Model Support**: The framework supports a wide range of language models, including popular models like BERT, RoBERTa, XLNet, and more.
- **Customizable**: Users can customize the optimization process by specifying their own objectives, constraints, and evaluation metrics.
- **Easy to Use**: With a simple and intuitive API, PrompTEA integrates easily with existing NLP pipelines.
- **Extensive Documentation**: PrompTEA comes with detailed tutorials, examples, and API references to help you get started quickly.
- **Scalability**: PrompTEA is designed to be scalable and can handle large-scale tasks in production environments.

## Installation

To install PrompTEA, simply run the following command:

```bash
pip install git+https://github.com/CodliRo/PrompTEA.git
```

Ensure that all the necessary dependencies are installed, and you're ready to start optimizing prompts with PrompTEA.

## Usage

Here's an example of how to use PrompTEA to optimize a prompt for sentiment analysis:

```python
import prompTEA

# Define the language model and task
model_name = "bert-base-uncased"
task_name = "sentiment-analysis"

# Define the prompt to optimize
prompt = "I love this product because"

# Optimize the prompt using PrompTEA
optimized_prompt = prompTEA.optimize_prompt(model_name, task_name, prompt)

print(optimized_prompt)
```
Here's an example of how to use PrompTEA in basic source:
In the file directory (`data/templates.json`), you can customize more prompt construction by using AI or you can optimze more by using my advices [Paper](https://dangnhutnguyen.github.io/Portfolio/#library)
```json
[   
    "Can you explain {prompt} in simple terms?",
    "How does {prompt} impact our daily lives?",
    "What are the benefits and drawbacks of {prompt}?",
    "Can you provide an example of {prompt} in action?",
    "How does {prompt} relate to {context}?",
    "What are the latest developments in {prompt} research?",
    "Can you compare and contrast {prompt} with {field}?",
    "How can {prompt} be used to improve {context}?",
    "What are the potential risks and challenges associated with {prompt}?"
    #you can customize more
]
```
Then , in the file directory (`main.py`), you can change your prompt in the (`original_prompt = "#your prompt here"`)
```python
from optimizers.prompt_optimizer import PromptOptimizer
def main():
    optimizer = PromptOptimizer()
    #input original prompt right here:
    original_prompt = "#your prompt here"
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
```
### Customization

PrompTEA provides the flexibility to customize the optimization process according to your specific needs. You can define objectives, constraints, and evaluation metrics to guide the optimization process. Here's an example:

```python
import prompTEA

# Define the language model and task
model_name = "bert-base-uncased"
task_name = "sentiment-analysis"

# Define the prompt to optimize
prompt = "I love this product because"

# Define the customization options
customization_options = {
    "objective": "maximize",              # The optimization goal
    "constraint": "length <= 10",         # Constraint on prompt length
    "evaluation_metric": "accuracy"       # Evaluation metric (e.g., accuracy, F1 score)
}

# Optimize the prompt using PrompTEA with customization options
optimized_prompt = prompTEA.optimize_prompt(model_name, task_name, prompt, customization_options)

print(optimized_prompt)
```
Yet, I've mentioned in Usage, you can customize templates in (`data/templates.json`), you can find more advanced templates by this one [Paper](https://dangnhutnguyen.github.io/Portfolio/#library)
### Available Customization Options:

- **Objective**: The goal of the optimization (e.g., maximize or minimize a specific metric).
- **Constraints**: Any restrictions or limits on the prompt (e.g., length, complexity).
- **Evaluation Metrics**: The metrics to assess the effectiveness of the optimized prompt (e.g., accuracy, F1 score).

## Contributing

We welcome contributions to PrompTEA! If you're interested in contributing, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your forked repository (`git push origin feature-branch`).
6. Submit a pull request describing your changes.

For larger contributions, please open an issue before submitting a pull request to discuss the proposed changes.

## License

PrompTEA is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank the developers of the language models and NLP libraries used in PrompTEA, including:

- [Hugging Face](https://huggingface.co/) for their transformers library.
- [PyTorch](https://pytorch.org/) for providing an efficient deep learning framework.

## Contact

For more information, please contact us at [insert contact email].

## Citing PrompTEA

If you use PrompTEA in your research or projects, please cite the following paper:

```bibtex
@article{prompTEA,
  title = {PrompTEA: A Prompt Optimization Framework for Language Models},
  author = {CodliRo},
  journal = {arXiv preprint},
  year = {2023}
}
```

## Roadmap

Here is a roadmap of the planned features and improvements for PrompTEA:

### Short-term:
- Improve the optimization algorithm to handle longer prompts.
- Add support for additional language models and NLP libraries.
  
### Medium-term:
- Develop a user-friendly interface for easier integration.
- Add support for multi-objective optimization (optimizing for multiple goals simultaneously).
  
### Long-term:
- Develop a framework for automated prompt optimization, reducing the need for manual tuning.
- Explore applications of PrompTEA in other NLP tasks like machine translation and question answering.

## Frequently Asked Questions (FAQs)

### Q: What is the purpose of PrompTEA?
**A**: PrompTEA is designed to optimize prompts for language models, improving their performance on specific tasks like sentiment analysis, text classification, and more.

### Q: How does PrompTEA work?
**A**: PrompTEA uses a combination of NLP techniques and machine learning optimization methods to generate effective prompts that elicit desired responses from language models.

### Q: Can I use PrompTEA for other NLP tasks?
**A**: Yes, PrompTEA can be applied to various NLP tasks such as text classification, sentiment analysis, machine translation, and more. The framework is highly customizable and can be adapted for different types of tasks.

### Q: Does PrompTEA support other language models besides BERT?
**A**: Yes, PrompTEA supports multiple language models, including BERT, RoBERTa, XLNet, and more. The framework is designed to be extensible, allowing support for additional models in the future.

### Q: Can I integrate PrompTEA into my existing NLP pipeline?
**A**: Absolutely! PrompTEA provides a simple and intuitive API, making it easy to integrate into your existing workflows.

**© 2025 Codliro. All Rights Reserved.**
This software is provided under the MIT License Agreement. Unauthorized use, duplication, or distribution is prohibited.

