# 🍽️ Zomato Data Analysis & Interactive Dashboard

🚀 **Live App:** https://zomato-data-analysis-cv5a.onrender.com

---

## 📌 Project Overview

This project focuses on analyzing restaurant data from Zomato to uncover insights about customer preferences, restaurant types, ratings, and ordering behavior.

The analysis is performed using Python and visualized through an **interactive Streamlit dashboard**, allowing users to explore the data dynamically.

---

## 🎯 Objectives

* Understand restaurant distribution by type
* Analyze customer voting patterns
* Study rating trends
* Compare online vs offline ordering behavior
* Identify cost preferences for couples
* Build an interactive dashboard for real-time insights

---

## 🛠️ Tech Stack

* **Python**
* **Pandas & NumPy** → Data Cleaning & Processing
* **Matplotlib & Seaborn** → Data Visualization
* **Streamlit** → Interactive Dashboard
* **Render** → Deployment

---

## 📂 Project Structure

```
zomato_analysis/
│
├── Zomato_Data_Analysis.py   # Streamlit App
├── Zomato_Data_Analysis.ipynb # Exploratory Analysis
├── Zomato-data-.csv          # Dataset
├── requirements.txt          # Dependencies
├── .gitignore                # Ignored files
└── README.md                 # Project Documentation
```

---

## 🧹 Data Cleaning & Preparation

* Converted `rate` column from string format (e.g., "4.2/5") to float
* Checked for missing/null values
* Standardized dataset for analysis

---

## 📊 Key Insights

### 1️⃣ Restaurant Type Distribution

* Majority of restaurants fall under **Dining category**

---

### 2️⃣ Votes Analysis

* Dining restaurants receive **highest number of votes**
* Indicates strong customer engagement

---

### 3️⃣ Online Order Availability

* Most restaurants **do NOT accept online orders**

---

### 4️⃣ Rating Distribution

* Most ratings fall between **3.5 to 4.0**
* Indicates generally good customer satisfaction

---

### 5️⃣ Cost for Two

* Most preferred cost range is around **₹300**
* Shows budget-friendly dining preference

---

### 6️⃣ Online vs Offline Ratings

* **Online orders → Higher ratings**
* **Offline orders → Slightly lower ratings**

---

### 7️⃣ Heatmap Insights

* Dining → Mostly offline orders
* Cafes → More online orders

👉 Suggests:

* People prefer **dining physically in restaurants**
* Prefer **online ordering for cafes**

---

## 📈 Dashboard Features

* ✅ Interactive filters (Restaurant Type, Online Orders)
* ✅ Dynamic visualizations
* ✅ Real-time data updates
* ✅ Clean and user-friendly UI

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/zomato-analysis.git
cd zomato-analysis
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run Zomato_Data_Analysis.py
```

---

## 🌐 Deployment

This project is deployed on **Render** using:

* Build Command:

```bash
pip install -r requirements.txt
```

* Start Command:

```bash
streamlit run Zomato_Data_Analysis.py --server.port $PORT --server.address 0.0.0.0
```

---

## 💡 Future Improvements

* Add **restaurant search functionality**
* Integrate **map-based visualization**
* Perform **customer segmentation analysis**
* Add **machine learning for rating prediction**

---

## 🧠 Learnings

* Hands-on experience with **data cleaning & preprocessing**
* Built interactive dashboards using **Streamlit**
* Understood real-world business insights from data
* Learned deployment using **Render**

---

## 🙌 Author

**Ankit Pandey**
🎓 B.Sc Data Science & Business Intelligence

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to connect!
