import pandas as pd 
from PIL import Image
import numpy as np
import os

csv_file_path= "../data/image_labels_preprocessed.csv"
image_folder_path = "../data/images_preprocessed"

# Remove images not listed in CSV file
def remove_unlisted():
    df = pd.read_csv(csv_file_path)
    # Get the set of file names listed in the CSV
    csv_file_names = set(f"{name}.jpg".lower() for name in df['image'])
    # Get the list of all image files in the folder
    image_files = set(os.listdir(image_folder_path))
    # Find files not in the CSV
    unlisted_files = image_files - csv_file_names
    # print(f"CSV:{len(csv_file_names)}")
    # print(f"image_files:{len(image_files)}")
    # print(f"unlisted files:{len(unlisted_files)}")
    for file_name in unlisted_files:
        file_path = os.path.join(image_folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            # print(f"Removed: {file_name}")
def list_unwanted_labels():
    df = pd.read_csv(csv_file_path)
    skip_images = df[df['label'] == 'Skip']
    skip_image_list = skip_images['image'].tolist()
    print("Images with label 'Skip':")
    print(skip_image_list)

    other_images = df[df['label'] == 'Other']
    other_image_list = other_images['image'].tolist()
    print("Images with label 'Other':")
    print(other_image_list)

def remove_unwanted_data():
    df = pd.read_csv(csv_file_path)
    if 'sender_id' in df.columns:
        df = df.drop(columns=['sender_id'])
    df_filtered = df[df['label'] != 'Not sure'] 
    df_filtered.to_csv(csv_file_path, index=False)

def normalize_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img_array = np.array(img) / 255.0 # Normalize to [0, 1]
    img_array = (img_array - 0.5) * 2 # Normalize to [-1, 1]
    return img_array

if __name__ == "__main__":
    remove_unwanted_data()

