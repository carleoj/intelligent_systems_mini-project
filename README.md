# Intelligent Systems Mini-Project

A machine learning mini-project developed for the course **CS 003 – Intelligent Systems**.  
This repository contains an experimental study that evaluates boosting-based classification models on stress-related questionnaire data.

## Overview
This project explores how different boosting algorithms perform on a dataset derived from the Stress subscale of a psychological questionnaire.  
All implementation, experimentation, and evaluation are contained within a single Jupyter Notebook.

## Contents
- **DASS Boosting.ipynb** – main notebook for data preprocessing, model training, hyperparameter search, and evaluation  
- Supporting Python and ML libraries (imported inside the notebook)

## Built With
- Python  
- pandas, numpy – data handling  
- scikit-learn – machine learning models  
- Jupyter Notebook – experiment environment

## Getting Started

### Prerequisites
Install the following dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn scipy imblearn joblib jupyter
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
