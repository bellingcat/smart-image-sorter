from pathlib import Path

def list_images(directory,  img_ext=('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
    directory = Path(directory)
    imgs_list = [file for file in directory.iterdir() if file.suffix.lower() in img_ext]
    imgs_list = [str(img) for img in imgs_list]
    return imgs_list

def setup_directories(source, destination, verbose=True):
    source_path = Path(source)
    destination_path = Path(destination)
    if source_path.exists():
        images = list_images(source_path)
        n_images = len(images)
        if n_images > 0:
            if verbose: print(f"Number of images in source directory: {n_images}")
        else:
            if verbose: print(f"No images found in source directory: {source_path}")
    else:
        return print(f"Source directory not found: {source_path}")
    
    # Destination
    if not destination_path.exists():
        destination_path.mkdir(parents=True)
        if verbose:
            print(f"Destination directory created: {destination_path}")
    else:
        if verbose:
            print(f"Destination directory exists: {destination_path}")

    return images
