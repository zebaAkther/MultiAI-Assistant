# 🤖 MultiAI Assistant

### *An All-in-One AI-Powered Multi-Task Application*

---
<img width="1245" height="704" alt="Screenshot 2026-05-03 at 10 41 12 PM" src="https://github.com/user-attachments/assets/f19b9c90-f402-4842-acb4-62b0d211d983" />

## 🚀 Overview

**MultiAI Assistant** is a unified AI platform that integrates multiple intelligent functionalities into a single application. It allows users to perform **NLP tasks, text generation, image classification, and emotion detection** seamlessly through an interactive interface.

This project demonstrates how multiple AI models can be combined into a **modular, scalable, and real-time system**.

---

## 🎯 Features

* 💬 **Sentiment Analysis** – Analyze text sentiment (Positive/Negative) with confidence score
* ✍️ **Text Generation** – Generate text based on user prompts using deep learning
* 🖼️ **Image Classification** – Upload images and classify objects in real-time
* 😊 **Emotion Detection** – Detect emotions from text with detailed probability breakdown
* 🎛️ **Dynamic Task Switching** – Switch between tasks using sidebar UI
* ⚡ **Real-time Predictions** – Fast inference using trained models

---

## 🧠 AI Modules

### 🔹 1. Sentiment Analysis

* Classifies user input into **positive or negative sentiment**
* Displays confidence score

📸 Example:

<img width="1245" height="717" alt="Screenshot 2026-05-03 at 10 49 53 PM" src="https://github.com/user-attachments/assets/caaac6b5-1f7e-46a2-96d8-ba7d8b7b6fb5" />

---

### 🔹 2. Text Generation

* Generates human-like text from prompts
* Uses sequence modeling (RNN/LSTM-based)

📸 Example:

<img width="1245" height="699" alt="Screenshot 2026-05-03 at 10 48 53 PM" src="https://github.com/user-attachments/assets/3f7f5615-dd9f-4bb7-a69f-453ca4e3f0d2" />


---

### 🔹 3. Image Classification

* Upload an image and get predicted label
* Uses deep learning-based image classification

📸 Example:

<img width="1246" height="706" alt="Screenshot 2026-05-03 at 10 50 53 PM" src="https://github.com/user-attachments/assets/fb3a116c-48f1-48e4-be2b-770fc5155e95" />

---

### 🔹 4. Emotion Detection

* Detects emotions like:

  * Joy
  * Anger
  * Sadness
  * Surprise
* Displays probability distribution

📸 Example:

<img width="1243" height="698" alt="Screenshot 2026-05-03 at 10 51 18 PM" src="https://github.com/user-attachments/assets/309d2e6c-9d7d-4162-a436-dc99b15ed846" />

---

## 🏗️ System Architecture

```text
User Input → Task Selector → Model Router → AI Module → Prediction → UI Output
```

---

## ⚙️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Libraries:**

  * TensorFlow / Keras
  * Scikit-learn
  * NumPy, Pandas
* **Computer Vision:** OpenCV / CNN
* **NLP:** Tokenization, Sequence Models

---

## 📂 Project Structure

```bash
MultiAI-Assistant/
│
├── app.py                  # Main Streamlit app
├── models/                 # Saved ML/DL models
├── modules/                # Individual AI modules
│   ├── sentiment.py
│   ├── text_generation.py
│   ├── image_classification.py
│   └── emotion_detection.py
├── assets/                 # Screenshots for README
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

```bash
git clone https://github.com/zebaAkther/MultiAI-Assistant.git
cd MultiAI-Assistant
```

```bash
python -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 Example Use Cases

* Analyze customer sentiment from reviews
* Generate text content automatically
* Classify images for quick identification
* Detect emotional tone in user input

---

## 📈 Key Highlights

* Combines **multiple AI domains** (NLP + CV)
* Modular and extensible architecture
* Real-time interactive UI
* Practical, end-to-end AI system

---

## ⚠️ Limitations

* Model accuracy depends on training data
* Limited scalability without backend optimization
* Basic models (can be upgraded to transformers/CNNs)

---

## 🔮 Future Enhancements

* 🔹 Add chatbot integration
* 🔹 Upgrade models to Transformers (BERT, GPT)
* 🔹 Deploy on cloud (Streamlit Cloud / AWS)
* 🔹 Add user authentication
* 🔹 API-based modular services

---

## 👩‍💻 Author

**Zeba Akther**
🔗 GitHub: https://github.com/zebaAkther

---



