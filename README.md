# ott-data-cleaning

# 🎬 OTT Entertainment Data Cleaning Project

## 📌 Project Overview
Data cleaning is the foundation of reliable data analysis. In this project, I simulated a raw, real-world "Streaming Analytics" dataset (like Netflix or Squid Game data) that contained common tracking issues: duplicates, inconsistent text formatting, corrupted date entries, and missing values. 

Using **Python** and **Pandas**, I systematically cleaned the dataset to ensure its accuracy, showcasing how "dirty data" can distort business metrics if left untreated.

---

## 🛠️ The Data Issues & How I Solved Them

| Column Affected | The Problem | The Impact | The Technical Fix (Pandas) |
| :--- | :--- | :--- | :--- |
| **Title** | Duplicate records for the same show. | Overinflated total viewership numbers by 20%. | `.drop_duplicates()` |
| **Category** | Mixed casing (`TV Show` vs `tv show`). | Broken aggregations; metrics would split the same group. | `.str.title()` |
| **Release_Date**| Messy text-string dates. | Impossible to track chronological trends or timeline plots. | `pd.to_datetime()` |
| **Director** | Null / Missing entry values. | Deleting rows completely would discard other valid data points. | `.fillna('Unknown Director')` |
