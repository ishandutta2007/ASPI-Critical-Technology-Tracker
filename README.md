# ASPI Critical Technology Tracker: Leadership Trends

A Python visualization tracking the shifting balance of global critical technology leadership between the United States and China from 2007 to 2025, based on dataset releases and reports from the **Australian Strategic Policy Institute (ASPI) Critical Technology Tracker**.

---

## 📊 Overview

The [ASPI Critical Technology Tracker](https://www.aspi.org.au/) monitors high-impact research across dozens of critical technologies (spanning defense, AI, space, robotics, energy, biotechnology, quantum computing, and advanced materials). 

This repository provides a lightweight script ([`aspi-tech-tracker-by-year.py`](file:///C:/Users/ishan/Documents/Projects/ASPI-Critical-Technology-Tracker/aspi-tech-tracker-by-year.py)) that plots the number of critical technologies led by China versus the United States over successive 5-year rolling windows.

### Dataset Window Summary

| Window Ending Year | Total Technologies Tracked | China Leads | US Leads | Other / Shared |
| :---: | :---: | :---: | :---: | :---: |
| **2007** (2003–2007) | 64 | 3 | 60 | 1 |
| **2017** (2013–2017) | 64 | 28 | 36 | 0 |
| **2022** (2018–2022) | 44 | 37 | 7 | 0 |
| **2023** (2019–2023) | 64 | 57 | 7 | 0 |
| **2024** (2020–2024) | 74 | 66 | 8 | 0 |
| **2025** (2021–2025) | 74 | 69 | 5 | 0 |

> *Note: Windows represent ending years of rolling 5-year evaluation periods as defined across ASPI dataset revisions.*

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [matplotlib](https://matplotlib.org/)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ishandutta2007/ASPI-Critical-Technology-Tracker.git
cd ASPI-Critical-Technology-Tracker
pip install matplotlib
```

### Usage

Run the visualization script:

```bash
python aspi-tech-tracker-by-year.py
```

---

## 📈 Chart Features

- **Country Comparisons**: Line series tracking technology dominance for China (red) and the United States (navy blue).
- **Benchmark Reference**: Dashed grey reference curve showing the total number of critical technologies tracked over time.
- **Annotated Data Points**: Clear fraction annotations (`leads / total`) at each evaluation milestone.
- **Publication Ready**: Clean layout with gridlines, custom color palette, and bottom-aligned legend.

---

## 📚 References & Attribution

- **Source**: [Australian Strategic Policy Institute (ASPI)](https://www.aspi.org.au/) – *Critical Technology Tracker*
- **Metric**: Leadership is determined by ASPI's methodology evaluating high-impact research publications (top 10% most-cited papers) and research institution rankings across tracked critical technology fields.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) (or public domain research / educational fair use).
