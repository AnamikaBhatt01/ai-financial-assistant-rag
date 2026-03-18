# 🚀 AI Financial Assistant (RAG + Analytics + Prediction)

## 📌 Overview

This project is an **AI-powered Financial Assistant** that transforms a traditional dataset/dashboard into an intelligent system capable of answering business questions, generating insights, and predicting future trends.

Instead of just viewing static dashboards, users can interact with the system using **natural language queries** and receive:

* 📊 Accurate calculations
* 🤖 Context-aware insights
* 🔮 Future predictions

---

## 🎯 Problem Statement

Traditional dashboards (like Power BI) are **static** and require manual analysis.

This project solves that by adding an **AI layer on top of financial data**, enabling:

* Faster decision-making
* Natural language interaction
* Automated insights

---

## ⚙️ Features

### 🟢 1. Financial Query Engine (Pandas)

* Computes exact values from data
* Example:

  * “Total profit”
  * “Profit by category”

---

### 🟡 2. RAG-based Insight Generation

* Uses Retrieval-Augmented Generation
* Retrieves relevant data and generates explanations
* Example:

  * “Why is furniture profit low?”
  * “Analyze profit trends”

---

### 🔵 3. Predictive Analytics (Machine Learning)

* Uses Linear Regression to forecast future values
* Example:

  * “Predict next month profit”

---

### 🧠 4. Intelligent Query Routing

* Detects user intent:

  * Calculation → Pandas
  * Prediction → ML Model
  * Explanation → RAG + LLM

---

## 🏗️ Architecture

```
User Query
   ↓
Intent Detection
   ↓
 ┌───────────────┬────────────────┬─────────────────┐
 │ RAG (FAISS)   │ Pandas Engine  │ ML Model        │
 │ explanation   │ exact calc     │ prediction      │
 └───────────────┴────────────────┴─────────────────┘
   ↓
LLM (Groq)
   ↓
Final Answer
```

---

## 🛠 Tech Stack

* **Python**
* **Pandas** (Data Analysis)
* **FAISS** (Vector Search)
* **Sentence Transformers** (Embeddings)
* **Groq API (LLM)**
* **Scikit-learn** (Machine Learning)

---

## 📂 Project Structure

```
├── main.py            # Main pipeline & chatbot
├── rag_engine.py      # Vector search using FAISS
├── analytics.py       # Financial calculations
├── prediction.py      # ML model for forecasting
├── intent.py          # Query classification
├── llm.py             # Groq LLM integration
├── text.py            # Data → text conversion
├── details.csv        # Dataset
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd ragPOWER
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the chatbot

```bash
python main.py
```

---

## 💬 Sample Queries

```
total profit
profit by category
which category is most profitable
predict next month profit
why is furniture profit low
```

---

## 📈 Sample Output

```
You: total profit  
Bot: Total profit is 36963  

You: predict next month profit  
Bot: Predicted next value profit: 5200  
```

---

## 🚀 Future Improvements

* Integration with Power BI dashboards
* Advanced forecasting models
* Real-time data pipelines
* Anomaly detection (money leak detection)
* Auto-generated business insights
## 💡 Key Learnings

* Combining **RAG + Analytics + ML** in one system
* Building an **end-to-end AI pipeline**
* Bridging gap between **Data Analysis and Generative AI**
## 🤝 Connect

If you found this interesting or want to collaborate, feel free to connect!
🔥 *This project demonstrates how AI can transform financial data into actionable intelligence.*
