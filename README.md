# 🖼️📁 Easy AI: zero-shot image classification 
[![Run in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/belisards/zeroshot_img_classifier/blob/main/interface.ipynb)

This repository provides a Python script and graphic user interface for zero-shot image classification using open-source models from [HuggingFace](https://huggingface.co/)'s library. 

The script organizes images into labelled folders based on the classification results. It can be used as a command-line tool or as a user interface in Jupyter Notebook.

You can test this tool with a set of 32 images extracted by Bellingcat from Telegram groups. The images are available in the `imgs/` folder.

## Features
- Zero-shot image classification using Hugging Face's models.

- Supports batch processing of images.

- Organizes images into folders based on their labels.

- Option to copy or move images after classification.

- Generates a CSV file with classification results.

## Graphic user interface

If you want to use the graphic user interface locally, make sure to enable the Jupyter Notebook extension for widgets:

```
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```

```
jupyter nbextension install --py widgetsnbextension --user
```

```
jupyter nbextension enable widgetsnbextension --user --py
```

This configuration above is automatically handled in [Google Colab](https://colab.research.google.com/github/belisards/zeroshot_img_classifier/blob/main/interface.ipynb).

## Command-Line 
Requires Python 3.10.

### Arguments
`--source`: Path to the source directory containing the images. Default is `imgs/`.

`--destination`: Path to the destination directory for classified images. Default is labeled/.

`--labels`: Comma-separated list of labels for classification.

`--operation`: Operation to perform on images after classification: `copy` or `move`. Default is `copy`.

`--model`: Model name for zero-shot classification. If not provided, the most download model for zero-shot image classification on HuggingFace will be used.

`--output_file`: Path to the CSV file for saving classification results. Default is `output.csv`.

`--batch_size`: Number of images to process in a batch. Default is `32`.

`--verbose`: Verbose output showing progress and model used. Default is `True`.

### Instructions
1. Clone the repository.

1. Follow the instructions to install Pytorch: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

1. Install the other required packages using `pip install -r requirements.txt`. Or use Poetry: `poetry install`.

1. Run the script replacing the arguments as needed:

`python classifier.py --source="imgs/" --destination="labeled/" --labels="cat,object" --operation="copy" --output_file="output.csv" --batch_size=32 --verbose=True`


