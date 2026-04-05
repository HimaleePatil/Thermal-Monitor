# 🔥 Thermal-Aware Process Monitor

A real-time system monitoring tool that visualizes CPU usage, analyzes running processes, and provides intelligent alerts to prevent system overheating.

---

## 📌 Overview

The **Thermal-Aware Process Monitor** is a GUI-based application developed using Python.
It continuously monitors CPU utilization, identifies high resource-consuming processes, and presents the data through an interactive dashboard.

Instead of directly reading hardware temperature sensors, this system uses CPU usage as an indicator of thermal behavior, making it lightweight and efficient.

---

## 🚀 Features

* 📊 **Real-Time CPU Monitoring**

  * Displays live CPU usage percentage

* 🌡️ **Thermal State Classification**

  * COOL 🟢 (<30%)
  * WARM 🟡 (30–70%)
  * HOT 🔴 (>70%)

* 📈 **Live Data Visualization**

  * Graph showing CPU usage over time

* 📋 **Process Analysis**

  * Displays top CPU-consuming processes

* 🔥 **Visual Usage Bars**

  * Graphical representation of process CPU usage

* 🚨 **Smart Alerts**

  * Popup warning for high CPU usage

* 💡 **Intelligent Suggestions**

  * Recommends actions like closing heavy applications

* 🔄 **Real-Time Updates**

  * Refreshes every 2 seconds

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries Used:**

  * `psutil` – system and process monitoring
  * `tkinter` – GUI development
  * `matplotlib` – data visualization

---

## 🏗️ System Architecture

```
CPU Data → psutil → Data Processing → GUI (Tkinter)
                             ↓
                     Visualization (Matplotlib)
```

---

## ▶️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/thermal-monitor.git
```

2. Navigate to project directory:

```
cd thermal-monitor
```

3. Install dependencies:

```
pip install psutil matplotlib
```

4. Run the application:

```
python main.py
```

---

## 🧪 How It Works

* The system fetches CPU usage using `psutil`
* Classifies system state into COOL, WARM, or HOT
* Displays top processes consuming CPU
* Updates data every 2 seconds
* Generates alerts when CPU usage exceeds threshold

---

## 📸 Screenshots

*Add your project screenshots here*

---

## 🎯 Use Cases

* System performance monitoring
* Identifying resource-heavy applications
* Preventing overheating
* Educational demonstration of OS concepts

---

## 🔮 Future Enhancements

* Integration with real temperature sensors
* Dark mode UI
* Process control (terminate/suspend)
* AI-based prediction of system load

---

## 🧠 Key OS Concepts Used

* Process Management
* CPU Scheduling
* Resource Monitoring
* System Performance Analysis

---

## 👩‍💻 Author

**Your Name**
GitHub: https://github.com/your-username

---

## 📄 License

This project is for educational purposes.
