# 🚗 Telematics-Based Usage Insurance System

A web-based application built using **Gradio + Python + MySQL** to analyze driving behavior and provide usage-based insurance premiums and safety feedback.

---

## 📌 Project Description

This project uses **telematics data** (e.g., speed, acceleration, braking) to:

- Analyze driver behavior
- Calculate risk scores
- Determine customized insurance premiums
- Provide safety feedback
- Store and retrieve records from a **MySQL database**

---

## 🚀 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core logic and backend |
| 🔥 Gradio | Web UI (simple alternative to Streamlit) |
| 🐬 MySQL | Data storage and retrieval |
| 🧠 Pandas | Table formatting |

---

## ✅ Features

- Manual input of telematics data via form
- Behavior analysis using domain logic
- Real-time premium calculation
- Safety feedback generation
- Full database integration using MySQL
- View all driver records in a dynamic table

---

## 🛠 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/telematics-insurance-gradio.git
cd telematics-insurance-gradio

### 2. Install Python Dependencies
```bash
pip install gradio mysql-connector-python pandas

### 3. Set Up MySQL Database
```sql
CREATE DATABASE telematics_insurance;

USE telematics_insurance;  

CREATE TABLE driving_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    speed FLOAT,
    acceleration FLOAT,
    braking FLOAT,
    distance_travelled FLOAT,
    behavior_score FLOAT,
    risk_score FLOAT,
    premium FLOAT,
    feedback TEXT
);

Then edit db.py and update your MySQL username/password:
```bash
user="root",
password="your_password"

### 4. 🧩 Install Gradio Extension for VS Code (Optional but Recommended)
Gradio has an official extension to easily preview and run your Gradio app inside VS Code:

Open VS Code

Go to Extensions (Ctrl+Shift+X)

Search for: "Gradio"

Install the extension by Gradio Team

Open app.py, right-click and select “Run Gradio App”

Or install from the VS Code Marketplace


▶️ Run the App
If you're not using VS Code extension:
```bash
python app.py

Then open in your browser: http://localhost:7860

| Driver ID | Speed | Acceleration | Braking | Distance |
| --------- | ----- | ------------ | ------- | -------- |
| 1         | 65    | 2.1          | 1.8     | 30       |

📂 Folder Structure
```bash
telematics_gradio/
├── app.py             # Main app file (Gradio interface)
├── db.py              # MySQL interaction logic
├── logic.py           # Core behavior and risk calculations

📄 License
MIT License © 2025 Angadi Anjali
```yaml

---

Would you like me to:
- Create a `requirements.txt` now?
- Generate the GitHub repository with this `README.md` included?

Let me know!




