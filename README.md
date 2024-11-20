
# Data Splitter and Validator

## Introduction
This project provides two Python scripts to streamline the process of splitting image-label datasets into training and validation sets (`Split.py`) and validating the consistency of these datasets (`Validate.py`). These scripts are designed for projects involving machine learning or computer vision, where organized and verified datasets are essential.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Split Script](#running-the-split-script)
  - [Running the Validation Script](#running-the-validation-script)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Usage

### Running the Split Script
1. **Prepare Your Data:**
   - Place images in the `IMG/` directory.
   - Place labels in the `LBL/` directory. Ensure label files have the same base name as their corresponding image files (e.g., `image1.jpg` and `image1.txt`).

2. **Run the script:**
   ```bash
   python Split.py
   ```

3. **Result:**
   - Images and labels are split into `images/train`, `images/val`, `labels/train`, and `labels/val`.

### Running the Validation Script
1. **Validate the Dataset:**
   ```bash
   python Validate.py
   ```

2. **Output:**
   - Counts of matched and mismatched files for training and validation sets.
   - List of mismatched files.

---

## Features
- **Dataset Splitting:** Organizes data into 70% training and 30% validation by default.
- **Validation:** Checks for mismatched images and labels in training and validation sets.
- **Error Reporting:** Outputs lists of mismatched files for debugging.

---

## Project Structure
```plaintext
project/
├── Split.py          # Script to split dataset
├── Validate.py       # Script to validate dataset
├── IMG/              # Directory for input images
├── LBL/              # Directory for input labels
├── images/           # Output directory for split images
│   ├── train/
│   └── val/
└── labels/           # Output directory for split labels
    ├── train/
    └── val/
```

---

## Dependencies
- Python 3.7+
- `scikit-learn`: For dataset splitting.
- `shutil`: For file operations (built-in).
- `os`: For directory management (built-in).

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
