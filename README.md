# Smart Image Sorter 🖼️📁

<a href="https://www.bellingcat.com"><img alt="Bellingcat logo: Discover Bellingcat" src="https://img.shields.io/badge/Discover%20Bellingcat-%20?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAYCAYAAADKx8xXAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TS0UqDnZQEcxQneyiIo6likWwUNoKrTqYXPoFTRqSFBdHwbXg4Mdi1cHFWVcHV0EQ%2FABxdnBSdJES%2F5cUWsR4cNyPd%2Fced%2B8AoVllqtkTA1TNMtKJuJjLr4rBVwQwhhBEDEvM1JOZxSw8x9c9fHy9i%2FIs73N%2Fjn6lYDLAJxLHmG5YxBvEs5uWznmfOMzKkkJ8Tjxp0AWJH7kuu%2FzGueSwwDPDRjY9TxwmFktdLHcxKxsq8QxxRFE1yhdyLiuctzir1Tpr35O%2FMFTQVjJcpzmKBJaQRIo6klFHBVVYiNKqkWIiTftxD%2F%2BI40%2BRSyZXBYwcC6hBheT4wf%2Fgd7dmcXrKTQrFgcCLbX%2BMA8FdoNWw7e9j226dAP5n4Err%2BGtNYO6T9EZHixwBA9vAxXVHk%2FeAyx1g6EmXDMmR%2FDSFYhF4P6NvygODt0Dfmttbex%2BnD0CWulq%2BAQ4OgYkSZa97vLu3u7d%2Fz7T7%2BwHEU3LHAa%2FQ6gAAAAZiS0dEAAAAAAAA%2BUO7fwAAAAlwSFlzAAAuIwAALiMBeKU%2FdgAAAAd0SU1FB%2BgFHwwiMH4odB4AAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAA50lEQVQ4y82SvWpCQRCFz25ERSJiCNqlUiS1b5AuEEiZIq1NOsGXCKms0wXSp9T6dskDiFikyiPc%2FrMZyf3FXSGQ0%2BzuzPl2ZoeVKgQ0gQ2wBVpVHlcDkjM5V%2FJ5nag6sJ%2FZX%2Bh%2FC7gEhqeAFKf7p1M9aB3b5oN1OomB7g1axUBPBr3GQHODHmOgqUF3MZAzKI2d4LWBV4H%2BMXDuJd1a7Cew1k7SwksaHC4LqNaw7aeX9GWHXkC1G1sTAS17Y3Kk2lnp4wNLiz0DrgLq8qt2MfmSSabAO%2FBBXp26dtrADPjOmN%2BAUdG7B3cE61l5hOZiAAAAAElFTkSuQmCC&logoColor=%23fff&color=%23000"></a><!--
--><a href="https://discord.gg/bellingcat"><img alt="Discord logo: Join our community" src="https://img.shields.io/badge/Join%20our%20community-%20?style=for-the-badge&logo=discord&logoColor=%23fff&color=%235865F2"></a><!--
--><a href="https://colab.research.google.com/github/bellingcat/smart-image-sorter/blob/main/interface.ipynb"><img alt="Colab icon: Try it on Colab" src="https://img.shields.io/badge/Try%20it%20on%20Colab-%20?style=for-the-badge&logo=googlecolab&logoColor=fff&logoSize=auto&color=e8710a"></a>

This repository provides a Python script and graphic user interface for zero-shot image classification using open-source models from [HuggingFace](https://huggingface.co/)'s library. 

The script organizes images into labelled folders based on the classification results. It can be used as a command-line tool or as a user interface in Jupyter Notebook.

You can test this tool with a set of 32 images extracted by Bellingcat from Telegram groups. The images are available in the `imgs/` folder.


## Features
- Zero-shot image classification using Hugging Face's models.

- Supports batch processing of images.

- Organizes images into folders based on their labels.

- Option to copy or move images after classification.

- Generates a CSV file with classification results.

### Instructions

Requires Python 3.10.

1. Clone the repository.

1. Follow the instructions to install Pytorch: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

1. Install the other required packages using `pip install -r requirements.txt`. Or use Poetry: `poetry install`.

1. Run the script replacing the arguments as needed:

`python classifier.py --source="imgs/" --destination="labeled/" --labels="cat,object" --operation="copy" --output_file="output.csv" --batch_size=32 --verbose=True`

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

This configuration above is automatically handled in [Google Colab](https://colab.research.google.com/github/bellingcat/smart-image-sorter/blob/main/interface.ipynb).


### Arguments
`--source`: Path to the source directory containing the images. Default is `imgs/`.

`--destination`: Path to the destination directory for classified images. Default is labeled/.

`--labels`: Comma-separated list of labels for classification.

`--operation`: Operation to perform on images after classification: `copy` or `move`. Default is `copy`.

`--model`: Model name for zero-shot classification. If not provided, the most download model for zero-shot image classification on HuggingFace will be used.

`--output_file`: Path to the CSV file for saving classification results. Default is `output.csv`.

`--batch_size`: Number of images to process in a batch. Default is `32`.

`--verbose`: Verbose output showing progress and model used. Default is `True`.




