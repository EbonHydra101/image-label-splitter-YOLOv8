# Image-Label-Splitter

**Image-Label-Splitter** is a Python tool that helps you split a dataset of images and their corresponding labels into training and validation sets. It ensures that:
- 70% of the images (and labels) are used for training.
- 30% of the images (and labels) are used for validation.
- If an image has no corresponding label, it is included in the training set without the label.

Additionally, the tool can validate that each image has a corresponding label in both the training and validation datasets.

---

## Features

- **Splits images and labels**: Automatically splits a folder of images (`IMG`) and a folder of labels (`LBL`) into separate `train` and `val` directories (70%/30% split).
- **Handles unmatched images**: If an image doesn't have a corresponding label, it will still be included in the training set.
- **Validation check**: Ensures that all images in `train` and `val` have matching label files, and outputs a report on mismatches.

---

## Getting Started

### Prerequisites

Before running the scripts, you need to have the following:

- **Python** (version 3.x): Download and install Python from [python.org](https://www.python.org/downloads/).
- **Required Python Libraries**: 
    - `shutil` and `os` (built-in Python libraries, no need to install)
    - `scikit-learn`: You can install it via pip:
      ```bash
      pip install scikit-learn
      ```

### Directory Structure

Ensure your dataset is structured like this:

