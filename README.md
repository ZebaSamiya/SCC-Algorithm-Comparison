# Comparative Analysis of Strongly Connected Component Algorithms  
### Kosaraju’s, Tarjan’s, and Parallel Approaches  

## Project Overview

This project investigates and compares three approaches for detecting **Strongly Connected Components (SCCs)** in directed graphs:

- **Kosaraju’s Algorithm**
- **Tarjan’s Algorithm**
- **Parallel SCC Detection Algorithm**

SCC detection is crucial in applications like **web crawling**, **social network analysis**, and **circuit design**. While traditional algorithms like Kosaraju’s and Tarjan’s offer efficient sequential solutions, they face limitations in performance and scalability on large graphs. Our project aims to evaluate how parallel algorithms can overcome these limitations.

---

## Objectives

- Implement Kosaraju’s, Tarjan’s, and one well-established parallel SCC detection algorithm.
- Use both **synthetic** and **real-world graph datasets** for evaluation.
- Compare each algorithm based on:
  - Execution Time ⏱️
  - Memory Usage 💾
  - Scalability on large/small-world graphs 📈
- Visualize and profile performance using Python tools.

---

## Technologies Used

- **Language:** Python 3.x
- **Libraries:** NetworkX, NumPy, Matplotlib, Pandas
- **IDE:** Visual Studio Code
- **Version Control:** Git + GitHub

---

## Project Structure

- **scc-algorithm-comparison/**
  -  **kosaraju/** → Kosaraju’s Algorithm Implementation
  -  **tarjan/** → Tarjan’s Algorithm Implementation
  -  **parallel/** → Parallel SCC Algorithm Implementation
  -  **datasets/** → Real-world and synthetic graph datasets
  -  **results/** → Performance results, charts, and logs
  -  **requirements.txt** → Python dependencies for the project
  -  **README.md** → Project overview and documentation

---

## License

This project is developed as part of an academic course and is intended for educational purposes only.

