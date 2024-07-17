import torch
import warnings
import pandas as pd
from transformers import pipeline
import argparse
from utils.file_manager import setup_directories, list_images
from utils.model import list_models, classify_images

warnings.filterwarnings("ignore")

def main():
    parser = argparse.ArgumentParser(description="Zero-shot image classification script")
    parser.add_argument('--source', type=str, default="imgs/", help="Path to the source directory containing the images")
    parser.add_argument('--destination', type=str, default="labeled/", help="Path to the destination directory where classified images will be copied or moved")
    parser.add_argument('--labels', type=str, required=True, help="Comma-separated list of labels for classification")
    parser.add_argument('--operation', type=str, choices=['copy', 'move'], default='copy', help="Operation to perform on images after classification: copy or move")
    parser.add_argument('--model', type=str, default=None, help="Model name for zero-shot classification. If not provided, the most popular model will be used.")
    parser.add_argument('--output_file', type=str, default="output.csv", help="Path to the CSV file where the classification results will be saved")
    parser.add_argument('--batch_size', type=int, default=32, help="Number of images to process in a batch")
    parser.add_argument('--verbose', type=bool, default=True, help="Verbose output showing progress and model used")

    args = parser.parse_args()

    images = setup_directories(args.source, args.destination, args.verbose)

    if len(images) == 0:
        print("No images found in source directory. Exiting...")
        return
    if args.model:
        model_name = args.model
    else:
        ALL_MODELS = list_models("zero-shot-image-classification")
        model_name = ALL_MODELS[0]
        

    labels = [label.strip() for label in args.labels.split(',')]
    
    classify_images(images, args.destination, model_name, labels, args.operation, args.output_file, args.batch_size, args.verbose)

if __name__ == "__main__":
    main()
