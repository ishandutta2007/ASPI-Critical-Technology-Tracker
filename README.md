# ASPI Critical Technology Tracker: US vs China Technology Leadership Trends (2007–2025)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Data: ASPI](https://img.shields.io/badge/Data-ASPI%20Tracker-red.svg)](https://www.aspi.org.au/)
[![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange.svg)](https://matplotlib.org/)

An open-source Python data visualization tracking the shifting balance of global critical and emerging technology leadership between the **United States** and **China** from 2007 through 2025. Data is sourced from research reports and dataset releases published by the **Australian Strategic Policy Institute (ASPI) Critical Technology Tracker**.

---

## 📌 Table of Contents

- [Overview & Background](#-overview--background)
- [Key Findings & Summary Data](#-key-findings--summary-data)
- [Critical Technology Categories](#-critical-technology-categories)
- [Chart Features](#-chart-features)
- [Installation & Quickstart](#-installation--quickstart)
- [Methodology & Data Sources](#-methodology--data-sources)
- [Keywords & Tags](#-keywords--tags)
- [Contributing & License](#-contributing--license)

---

## 📊 Overview & Background

The **[ASPI Critical Technology Tracker](https://www.aspi.org.au/)** is a landmark research initiative monitoring high-impact scientific research and technological capability across dozens of critical, dual-use, and emerging technologies. The tracker evaluates which countries and institutions lead the world in high-impact research publications (top 10% most-cited publications) across key domains.

This repository provides a standalone Python script ([`aspi-tech-tracker-by-year.py`](file:///C:/Users/ishan/Documents/Projects/ASPI-Critical-Technology-Tracker/aspi-tech-tracker-by-year.py)) utilizing `matplotlib` to chart the strategic inflection point where China surpassed the United States across successive 5-year rolling evaluation cohorts.

---

## 📈 Key Findings & Summary Data

The table below summarizes technological leadership across successive ASPI evaluation windows:

| Window Ending Year | Evaluation Period | Total Technologies Tracked | China Leads | US Leads | Other / Shared | Key Trend |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **2007** | 2003–2007 | 64 | 3 | 60 | 1 | Clear US global research dominance |
| **2017** | 2013–2017 | 64 | 28 | 36 | 0 | Rapid rise in Chinese high-impact research |
| **2022** | 2018–2022 | 44 | 37 | 7 | 0 | China overtakes US across majority of fields |
| **2023** | 2019–2023 | 64 | 57 | 7 | 0 | Expansion to 64 critical technologies |
| **2024** | 2020–2024 | 74 | 66 | 8 | 0 | Expanded coverage including advanced materials & biotech |
| **2025** | 2021–2025 | 74 | 69 | 5 | 0 | China leads in 69 of 74 tracked critical technologies |

> **Note**: Window years represent the ending year of rolling 5-year publication analysis periods defined by ASPI dataset updates.

---

## 🔬 Critical Technology Categories

The tracker encompasses technologies across major strategic and defense sectors:

- **Artificial Intelligence (AI) & Computing**: Advanced algorithms, natural language processing, machine learning, high-performance computing, advanced data analytics.
- **Quantum Technologies**: Quantum computing, quantum communications, quantum sensors.
- **Advanced Materials & Manufacturing**: Nanomaterials, metamaterials, advanced composites, smart materials, additive manufacturing.
- **Biotechnology, Gene & Vaccines**: Synthetic biology, genomic sequencing, novel vaccines, biomanufacturing.
- **Defense, Space & Robotics**: Autonomous systems, drones, hypersonic systems, satellite positioning, directed energy technologies.
- **Energy & Environment**: Advanced batteries, photovoltaics, hydrogen energy, nuclear energy, carbon capture.
- **Telecommunications & Sensing**: 5G/6G, advanced optical communications, advanced radar, sonar.

---

## 🚀 Installation & Quickstart

### Prerequisites

- Python 3.8 or higher
- [matplotlib](https://matplotlib.org/)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ishandutta2007/ASPI-Critical-Technology-Tracker.git
   cd ASPI-Critical-Technology-Tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install matplotlib
   ```

3. **Run the visualization:**
   ```bash
   python aspi-tech-tracker-by-year.py
   ```

---

## 📉 Chart Features & Visualization Design

- **Bilateral Comparison**: Tracks China (red) and the United States (navy blue) trajectories.
- **Benchmark Baseline**: Dashed grey reference curve illustrating total technologies tracked over time.
- **Fractional Annotations**: Displays explicit fraction scores (`leads / total tracked`) at each evaluation year.
- **Publication-Ready Styling**: Clean presentation with custom typography, grid layout, and bottom-aligned legend.

---

## 📚 Methodology & Data Sources

- **Source Organization**: [Australian Strategic Policy Institute (ASPI)](https://www.aspi.org.au/) – *Critical Technology Tracker Policy Briefs & Datasets*.
- **Evaluation Metric**: Global technology leadership is calculated based on:
  - Top 10% most-cited research publications across peer-reviewed literature.
  - Institutional H-index and global talent flow / research concentration metrics.
  - Tracked technology datasets expanded from 44 to 74 critical technologies over successive updates.

---

## 🏷️ Related Keywords & Search Terms

`aspi-critical-technology-tracker` • `critical-technologies` • `us-china-tech-competition` • `geopolitics` • `data-visualization` • `matplotlib` • `technology-policy` • `emerging-technologies` • `ai-leadership` • `quantum-computing` • `science-and-technology-policy` • `python-chart`

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE). Sourced data and metrics belong to their respective authors at the Australian Strategic Policy Institute (ASPI).
