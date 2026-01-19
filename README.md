# Academic Performance Prediction: ML Project

Pablo Berástegui Magallón (202311460)
Mathematical Engineering and Artificial Intelligence
Universidad Pontificia Comillas

## Main project files

* **notebooks/**: Contains the Jupyter notebooks (`.ipynb`) used for the analysis and development of the project. Each notebook is documented and corresponds to a specific stage of the workflow:

  * `exploration.ipynb`: Data cleaning, preparation, and visualization.
  * `models.ipynb`: Implementation and evaluation of all models.
  * `test_prep.ipynb`: Preparation of the test data for prediction.
* **data/**: Folder containing the datasets used, both raw and processed.
* **src/**: Source code with auxiliary functions and reusable scripts.

  * `utils.py`: Includes a custom visualization function and mapping dictionaries.

## Overview

This project focuses on predicting the final grade (`T3`) of secondary school students using sociodemographic, academic, and behavioral variables. Both supervised and unsupervised machine learning techniques are applied under two modeling approaches:

* **Model (i)**: Uses all available variables, including prior grades `T1` and `T2`.
* **Model (ii)**: Excludes `T1` and `T2`, aiming to anticipate academic performance before the student has been formally assessed.

**Note**: scikit-learn implementations were used for simplicity, syntactic consistency, and computational efficiency.
