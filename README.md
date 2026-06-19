#  Data Portfolio: Analytics & Algorithms

Welcome to my portfolio! This repository showcases my transition from foundational data cleaning techniques into core computer science concepts like Data Structures and Algorithms (DSA).

---

##  Project 1: OTT Entertainment Data Cleaning
Data cleaning is the foundation of reliable data analysis. In this project, I simulated a raw "Streaming Analytics" dataset containing tracking duplicates, inconsistent casing, and missing values, and cleaned it systematically using Python and Pandas.

###  The Data Issues & How I Solved Them
| Column Affected | The Problem | The Impact | The Technical Fix (Pandas) |
| :--- | :--- | :--- | :--- |
| **Title** | Duplicate records. | Overinflated total metrics by 20%. | `.drop_duplicates()` |
| **Category** | Mixed casing (`tv show`). | Broken data aggregations. | `.str.title()` |
| **Release_Date**| Messy text-string dates. | Impossible to track timelines. | `pd.to_datetime()` |
| **Director** | Null / Missing fields. | Row deletion would discard valid data. | `.fillna('Unknown')` |

---

##  Project 2: Efficient Processing with Binary Search (DSA)
As datasets grow into millions of rows, scanning data row-by-row becomes too slow. This project implements **Binary Search**—a core algorithm designed to search sorted lists with maximum performance.

###  Concept Strategy
Instead of inspecting items sequentially ($O(N)$ time complexity), Binary Search cuts the data space in half with each iteration ($O(\log N)$ time complexity). 

* **File Implemented:** `binary_search.py`
* **Use Case:** Instantly looking up specific User IDs from a sorted dataset.
* **Key Terms Handled:** Divide and conquer, mid-point evaluation, pointers (`left`, `right`).

---

A great data professional doesn't just clean the data—they understand how to manipulate and retrieve it with peak efficiency.
