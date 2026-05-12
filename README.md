# 🇮🇳 India Census Data Visualization Dashboard

An interactive geospatial dashboard built with **Streamlit** and **Plotly** to explore India's 2011 Census data at the district level — visualized on a live map with customizable primary and secondary parameters.

🔗 **Live Demo:** [https://zedtngyhun4gwwe5oxeaq8.streamlit.app/](https://zedtngyhun4gwwe5oxeaq8.streamlit.app/)

---

## 📌 About the Project

This dashboard allows users to explore socio-demographic data from India's 2011 Census across states and districts. Using an interactive scatter mapbox, you can select any state (or view all of India at once) and compare two census parameters visually — one controlling bubble **size** and the other controlling bubble **color**.

It's a lightweight yet powerful tool for anyone interested in data journalism, public policy research, or just exploring how India looked demographically in 2011.

---

## ✨ Features

- 🗺️ **Interactive Map** — Scatter mapbox powered by Plotly, centered on India
- 🏙️ **District-level Granularity** — Hover over any district to see its name
- 📊 **Dual Parameter Comparison** — Choose a primary (size) and secondary (color) census metric simultaneously
- 🔍 **State Filter** — Zoom into any individual state or view the entire country
- ⚡ **Fast & Lightweight** — Runs entirely in the browser via Streamlit

---

## 🖥️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app framework |
| Plotly Express | Interactive map visualization |
| Pandas | Data loading and manipulation |
| NumPy | Numerical support |

---

## 📁 Project Structure

```
a-data-viz-dashboard/
│
├── app.py              # Main Streamlit application
├── india.csv           # India 2011 Census dataset (district-level)
├── requirements.txt    # Python dependencies
└── .devcontainer/      # Dev container configuration
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/prathameshajabe/a-data-viz-dashboard.git
cd a-data-viz-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📦 Requirements

```
numpy
pandas
plotly
streamlit
```

---

## 🗂️ Dataset

The `india.csv` file contains district-level data from the **2011 Census of India**, including columns for:
- State and District names
- Latitude and Longitude (for map plotting)
- Various demographic metrics (population, literacy rate, sex ratio, etc.)

---

## 📸 How to Use

1. Open the sidebar on the left
2. Select a **State** (or keep "Overall" for all of India)
3. Choose a **Primary parameter** — this controls the **size** of the bubbles
4. Choose a **Secondary parameter** — this controls the **color** of the bubbles
5. Click **"Plot Graph"** to render the map

> 💡 *Larger bubbles = higher value of primary parameter. Darker/different colors = variation in secondary parameter.*

---

## 🌐 Live App

Try it out without any installation:

👉 [https://zedtngyhun4gwwe5oxeaq8.streamlit.app/](https://zedtngyhun4gwwe5oxeaq8.streamlit.app/)

---

## 🙋‍♂️ Author

**Prathamesh Ajabe**
- GitHub: [@prathameshajabe](https://github.com/prathameshajabe)

---


