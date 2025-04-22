# Split dataset into valuation and training sets
# Import necessary libraries
import os
import re
import shutil
import random
from pathlib import Path


# Path to the dataset
source_dir = "D:\Guvi Projects\Mini Project - 5\Faulty_solar_panel"
target_dir = "D:\Guvi Projects\Mini Project - 5\Faulty_solar_panels_proccessed"
train_dir = os.path.join(target_dir, "train")
val_dir = os.path.join(target_dir, "val")

# Train and validation split ratio
train_ratio = 0.8

# Make directories for train and val sets
def create_dir_structure(base_dir, class_names):
    for split in ["train", "val"]:
        split_dir = os.path.join(base_dir, split)
        os.makedirs(split_dir, exist_ok=True)
        for class_name in class_names:
            class_dir = os.path.join(split_dir, class_name)
            os.makedirs(class_dir, exist_ok=True)

# Split the dataset into train and val sets
def split_dataset():
    # Get the list of class names (subdirectories) in the source directory 
    class_names = os.listdir(source_dir)
    create_dir_structure(target_dir, class_names)

    for class_name in class_names:
        class_path = os.path.join(source_dir, class_name)
        images = os.listdir(class_path)
        random.shuffle(images)

        # Calculate the number of training and validation samples
        num_train = int(len(images) * train_ratio)
        train_images = images[:num_train]
        val_images = images[num_train:]

        # Copy the images to the respective directories
        for image in train_images:
            src_path = os.path.join(class_path, image)
            dst_path = os.path.join(train_dir, class_name, image)
            shutil.copy(src_path, dst_path)

        for image in val_images:
            src_path = os.path.join(class_path, image)
            dst_path = os.path.join(val_dir, class_name, image)
            shutil.copy(src_path, dst_path)

# Run the split_dataset function
if __name__ == "__main__":
    split_dataset()
    # print("Dataset split into training and validation sets successfully.")
    # print(f"Training set: {len(os.listdir(train_dir))} images")
    # print(f"Validation set: {len(os.listdir(val_dir))} images")
    # print("Directory structure created successfully.")
    # print("Training and validation sets created successfully.")

# The dataset has been split into training and validation sets, 
# and the directory structure has been created successfully.

# The training set contains 80% of the images, and the validation set contains 20%.

# -----------------------------------------------------------------------------------------------------------


