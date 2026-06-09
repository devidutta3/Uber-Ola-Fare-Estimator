# 🚖 Uber-Ola Fare Estimator

A lightweight Python project for exploring and preparing ride fare data from Uber and Ola trips. This repository includes dataset inspection, data cleaning, and a simple preprocessing flow for fare estimation analysis.

---

## 🌟 Project Overview

This repository demonstrates a minimal end-to-end workflow for working with taxi fare data:

- `src/train.py` loads the dataset, inspects structure, and performs initial cleaning steps.
- `src/EDA.py` conducts exploratory data analysis and reviews fare distributions.
- `Data/uber.csv` is the source dataset containing ride information for fare estimation.

---

## 📁 Repository Structure

- `Data/uber.csv` — raw ride dataset used for analysis.
- `src/train.py` — data loading and preprocessing script.
- `src/EDA.py` — exploratory analysis and fare filtering.
- `requirements.txt` — project dependencies.

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/Uber-Ola-Fare-Estimator.git
cd Uber-Ola-Fare-Estimator
```

2. Create and activate a virtual environment:

```powershell
python -m venv .env
.\.env\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install pandas
```

> Note: `requirements.txt` currently includes plotting-related packages. `pandas` is required for dataset loading and analysis.

---

## ▶️ How to Run

Run the preprocessing and inspection scripts from the project root:

```bash
python src\train.py
python src\EDA.py
```

- `src/train.py` prints dataset preview, column metadata, and cleaned shape.
- `src/EDA.py` filters invalid fares and provides a simple exploratory output.

---

## 🧠 What It Does

- Loads the Uber/Ola CSV dataset.
- Displays the first rows and dataset information.
- Detects missing and duplicate values.
- Drops unnecessary columns: `Unnamed: 0`, `key`.
- Removes rows with missing values.
- Filters out non-positive fares in the EDA flow.

---

## 💡 Improvements

Future enhancements could include:

- building a machine learning fare prediction model
- adding visualization of pickup/dropoff distributions
- validating geographic coordinates and trip distance
- converting the explorer into a notebook or dashboard

---

## 📌 Notes

- Ensure `Data/uber.csv` is present before running scripts.
- This project is ideal for exploratory data preparation and as a foundation for fare prediction modeling.

---

## 📜 License & Credit

This project is licensed under the Apache License 2.0. By using or sharing this repository, please give credit to the original programmer.

If you reuse this code or build upon it, include a note that credits the original author of the repository.
