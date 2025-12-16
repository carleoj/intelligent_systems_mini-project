# Intelligent Systems Mini-Project

A machine learning mini-project developed for the course **CS 003 – Intelligent Systems**.  
This repository contains an experimental study that evaluates boosting-based classification models on the DASS-21 questionnaire data.

## Overview
This project explores how different boosting algorithms perform on a dataset derived from the DASS-21 questionnaire.  
All implementation, experimentation, and evaluation are contained within a single Jupyter Notebook.

## Contents
- **DASS Boosting.ipynb** – main notebook for data preprocessing, model training, hyperparameter search, and evaluation  
- Supporting Python and ML libraries (imported inside the notebook)

## Built With
Python – Core programming language used for implementation and experimentation
pandas (v2.3.1) – Tabular data manipulation, preprocessing, and analysis
NumPy (v2.0.2) – Numerical computing and array-based operations
scikit-learn (v1.6.1) – Machine learning models, evaluation metrics, and preprocessing utilities
Matplotlib (v3.9.4) – Data visualization and plotting of experimental results
Seaborn (v0.13.2) – Statistical data visualization built on top of Matplotlib
SciPy (v1.13.1) – Scientific computing utilities, including optimization and statistical functions
imbalanced-learn (v0.0) – Handling class imbalance through resampling techniques (e.g., SMOTE)
Joblib (v1.5.1) – Model serialization and parallel computation support
Jupyter Notebook (v7.4.5) – Interactive development and experimentation environment

## Getting Started

### Prerequisites
Install the following dependencies:
```bash
pip install pandas==2.3.1
pip install numpy==2.0.2
pip install scikit-learn==1.6.1
pip install matplotlib==3.9.4
pip install seaborn==0.13.2
pip install scipy==1.13.1
pip install imblearn==0.0
pip install joblib==1.5.1
pip install notebook==7.4.5
```

## Algorithms

Install the boosting algorithms:
- XGBoost Version: 2.1.4
- CatBoost Version: 1.2.8
- LightGBM Version: 4.6.0

```
pip install xgboost==2.1.4
pip install catboost==1.2.8
pip install lightgbm==4.6.0
```
or 
```
conda install -c conda-forge xgboost=2.1.4
conda install -c conda-forge catboost=1.2.8
conda install -c conda-forge lightgbm=4.6.0
```
## Dataset

The dataset used in this project is sourced from Mendeley Data: https://data.mendeley.com/datasets/br82d4xkj7/1
- Dataset Title: Mental Health dataset based on DASS-21

- The dataset is provided in CSV format and must be placed in the project directory

## Running the Notebook

### Clone the Repository
git clone https://github.com/carleoj/intelligent_systems_mini-project.git

### Navigate to the project folder and launch Jupyter:
cd intelligent_systems_mini-project
jupyter notebook

- #### Open DASS Boosting.ipynb and run all cells to reproduce the experiment.



Regards,
Carl P.
