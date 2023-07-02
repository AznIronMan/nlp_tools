# nlp_tools

by [ClarkTribeGames, LLC](https://www.clarktribegames.com)

`nlp_tools` This repository contains Python scripts for Natural Language Processing tasks, using the Hugging Face Transformers library. The tasks include emotion detection from text, extracting keywords from text, and summarizing text.

## Prerequisites

- Windows, macOS, or Linux machine with Python 3.8 or later installed.
- Local Administrator rights (Windows) or `sudo` access (macOS/Linux).
- Internet Connection (for the initial model downloads).

## Clone Repo

You can clone this repo into any location you like and run it from anywhere. Run these commands in your terminal:

```bash
cd /path_of_your_choice
git clone https://github.com/AznIronMan/nlp_tools.git
```

## Setup virtual Python environment

We recommend using Anaconda for your virtual python environment:

```bash
cd /path_of_your_choice
conda create -n nlp_tools
conda activate nlp_tools
```

Be sure that you have your env name before your prompt (e.g. **(nlp_tools)** /filepath/ # )

## Install Dependencies

You will need a NVIDIA card for this. Install the appropriate Pytorch Cuda package from [https://pytorch.org/](https://pytorch.org/)

This is the bash command we used:

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

Then install the required Python libraries for this project, use the `requirements.txt` file with pip:

```bash
cd /path_of_your_choice
pip install -r requirements.txt
```

## Scripts

This repository contains the following Python scripts:

- `emotions.py` - Uses the Transformers library to classify the emotion of a given text.
- `keywords.py` - Extracts keywords from the provided text using T5 model.
- `summarizer.py` - Summarizes the given text using the BART model.

Each script can be run from the command line with additional arguments to specify the input text and other parameters.

# Usage

Emotion Detection `emotions.py`

```bash
python emotions.py "<Your Text Here>"
```

Keywords Extraction `keywords.py`

```bash
# num_beams = how many words you want per 'keyword' / # max_tokens is the max number of tokens for your response
# num_beams and max_tokens are optional arguments - they default to 3 and 4096 respectively
python keywords.py "<Your Text Here>" [num_beams] [max_tokens]
```

Text Summarization `summarizer.py`

```bash
# threshold is the minimum word count to be considered for summarization - anything under this number will not be summarized - default: 32 (optional)
# curve is the decimal that the word count is multiplied by to get the percentage for max and min length when max and min are invalid - default: 0.1 (optional)
# max_length defaults to None (optional) / min_length defaults to None (optional) -- these values being None = use of curve
python summarizer.py "<Your Text Here>" [max_length] [min_length] [threshold] [curve]
```

**Note:** Please replace `<Your Text Here>` with your input text.
**Also Note:** For `keywords.py` and `summarizer.py`, the additional arguments are optional and have default values if not specified.

## Dependencies

Here is a list of Python libraries used in this project:

- Transformers
- Torch
- Numpy
- tqdm
- requests
- regex
- urllib3
- PyYAML
- typing
- certifi
- charset-normalizer
- colorama
- filelock
- fsspec
- huggingface-hub
- idna
- Jinja2
- MarkupSafe
- mpmath
- mypy-extensions
- networkx
- packaging
- Pillow
- pyre-extensions
- sentencepiece
- sympy
- tokenizers
- torchaudio
- torchvision
- typing-inspect
- typing_extensions
- xformers

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Contact

Discord: `AznIronMan`
E-Mail: **geoff** `at` **clark tribe games** `dot` **com** (_no spaces and replace at with @ and dot with ._)
