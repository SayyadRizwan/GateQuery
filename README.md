# 🎓 GateQuery

### AI-Powered GATE Previous Year Question Analyzer

<p align="center">
  <b>Search • Retrieve • Analyze • Learn</b>
</p>

<p align="center">
  <a href="https://sayyadrizwan-gatequery-app-jxwoef.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo">
  </a>
  <a href="https://github.com/SayyadRizwan/GateQuery">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-0467DF?style=flat-square">
  <img src="https://img.shields.io/badge/RAG-AI_System-8A2BE2?style=flat-square">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">
</p>

---

## 🌐 Live Application

<p align="center">

### 🚀 [Launch GateQuery](https://sayyadrizwan-gatequery-app-jxwoef.streamlit.app/)

**Ask about a GATE topic → Retrieve relevant PYQs → Analyze concepts**

</p>

---

# 💡 What is GateQuery?

**GateQuery** is an AI-powered **GATE Previous Year Question (PYQ) Analyzer** built using **Retrieval-Augmented Generation (RAG)** and **semantic vector search**.

Instead of manually searching through hundreds of GATE papers, simply enter a concept or topic:

```text
Binary Search Tree
```

or

```text
Deadlock in Operating Systems
```

GateQuery finds the most semantically relevant GATE questions from its knowledge base.

### 🎯 The goal

> **Turn a large collection of GATE PYQs into an intelligent, searchable learning system.**

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔍 Semantic Search
Find questions based on **meaning and context**, not just exact keywords.

</td>

<td width="50%">

### 🤖 RAG Pipeline
Uses retrieved questions as contextual knowledge for intelligent analysis.

</td>
</tr>

<tr>
<td>

### ⚡ FAISS Retrieval
Fast similarity search using a vector database.

</td>

<td>

### 🧠 Sentence Transformers
Uses `all-MiniLM-L6-v2` to generate compact semantic embeddings.

</td>
</tr>

<tr>
<td>

### 📚 GATE PYQ Knowledge Base
Search through a structured collection of previous-year questions.

</td>

<td>

### 🌐 Interactive UI
Clean and simple Streamlit interface for querying the system.

</td>
</tr>
</table>

---

# 🧠 How GateQuery Works

```text
                    👤 USER
                      │
                      │
                      ▼
             ┌─────────────────┐
             │   Enter Query   │
             │ "BST in GATE"   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Query Embedding │
             │ Sentence        │
             │ Transformers    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   FAISS Index   │
             │ Vector Search   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Relevant GATE   │
             │ PYQs Retrieved  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   RAG Analyzer  │
             │ Context + Query │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Streamlit UI   │
             │ Final Results    │
             └─────────────────┘
```

---

# 🏗️ System Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                         GATEQUERY                            │
└──────────────────────────────────────────────────────────────┘

       GATE PAPERS
            │
            ▼
   ┌───────────────────┐
   │ Data Collection   │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Question / Answer │
   │ Extraction        │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Data Processing   │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Sentence          │
   │ Transformer       │
   │ Embeddings        │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ FAISS Vector      │
   │ Index              │
   └─────────┬─────────┘
             │
             │
       USER QUERY
             │
             ▼
   ┌───────────────────┐
   │ Semantic Retrieval│
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ RAG Analyzer      │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Streamlit         │
   │ Frontend          │
   └───────────────────┘
```

---

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| 🐍 Language | Python |
| 🎨 Frontend | Streamlit |
| 🧠 Embeddings | Sentence Transformers |
| 🔎 Vector Search | FAISS |
| 🤖 Architecture | RAG |
| 📊 Data Processing | Pandas / NumPy |
| 📚 Dataset | GATE Previous Year Questions |
| 🚀 Deployment | Streamlit Community Cloud |

### Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

**Embedding Dimension:** `384`

---

# 📊 Current Knowledge Base

<div align="center">

| Metric | Value |
|:---:|:---:|
| 📚 Questions | **390** |
| 🧠 Vector Embeddings | **390** |
| 📐 Embedding Dimension | **384** |
| ✅ Matched Answers | **170** |
| 🔎 Vector Index | **FAISS** |

</div>

---

# 🔎 Example Queries

Try asking GateQuery:

```text
Binary Search Tree
```

```text
Operating System Deadlock
```

```text
DBMS Normalization
```

```text
TCP Congestion Control
```

```text
Graph Traversal
```

```text
Compiler Parsing
```

```text
Cache Memory
```

The system retrieves questions that are **semantically related** to the query.

---

# 📂 Project Structure

```text
GateQuery/
│
├── 📄 app.py
├── 📄 rag.py
├── 📄 build_idx.py
├── 📄 download_data.py
├── 📄 extract_answers.py
├── 📄 merge_questions_answers.py
├── 📄 requirements.txt
│
├── 📁 data/
│   ├── 📁 papers/
│   └── 📁 vector_store/
│       └── questions.index
│
└── 📄 README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SayyadRizwan/GateQuery.git
cd GateQuery
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

# 🚀 Deployment

GateQuery is deployed using **Streamlit Community Cloud**.

### Live URL

👉 **https://sayyadrizwan-gatequery-app-jxwoef.streamlit.app/**

---

# 🔄 Data Pipeline

```text
        GATE SOURCES
             │
             ▼
      Download Papers
             │
             ▼
     Extract Questions
             │
             ▼
      Extract Answers
             │
             ▼
    Match Q&A Pairs
             │
             ▼
   Generate Embeddings
             │
             ▼
       FAISS Index
             │
             ▼
       RAG Retrieval
             │
             ▼
       Streamlit UI
```

---

# 🧪 Example Workflow

### User

```text
What are the important concepts related to BST in GATE?
```

### GateQuery

```text
        Query
          │
          ▼
     Embedding
          │
          ▼
   Semantic Search
          │
          ▼
   Relevant PYQs
          │
          ▼
      Analysis
```

The system can then surface the most relevant previous-year questions from the knowledge base.

---

# 🔮 Future Improvements

GateQuery can be extended with:

- 📈 Topic-wise GATE analytics
- 📊 Difficulty prediction
- 🗓️ Year-wise filtering
- 📚 Subject-wise filtering
- 🎯 Topic frequency analysis
- 🧠 LLM-powered explanations
- 💬 Conversational RAG
- 🔗 Graph-RAG integration
- 📌 Question bookmarking
- 📈 Performance tracking
- 📝 Personalized practice sets
- 🎓 AI-generated mock tests

---

# 🎯 Why GateQuery?

Traditional PYQ preparation:

```text
Search PDF
   ↓
Find topic
   ↓
Open question
   ↓
Repeat
```

GateQuery:

```text
Ask a question
      ↓
Semantic Retrieval
      ↓
Relevant PYQs
      ↓
Learn the concept
```

### 🚀 From PDF searching → AI-powered retrieval.

---

# 👨‍💻 Author

<div align="center">

### **Rizwan Sayyad**

B.Tech — AI & ML / CSE-AIML

Interested in:

**Machine Learning • Deep Learning • NLP • Generative AI • RAG • DSA**

[![GitHub](https://img.shields.io/badge/GitHub-SayyadRizwan-181717?style=for-the-badge&logo=github)](https://github.com/SayyadRizwan)

</div>

---

# ⭐ Show Your Support

If you found **GateQuery** useful, consider giving the repository a ⭐.

<p align="center">

### ⭐ Star the Repository

**[github.com/SayyadRizwan/GateQuery](https://github.com/SayyadRizwan/GateQuery)**

### 🚀 Try the Application

**[Launch GateQuery](https://sayyadrizwan-gatequery-app-jxwoef.streamlit.app/)**

</p>

---

<p align="center">
  <b>Built with Python 🐍 • RAG 🤖 • FAISS 🔎 • Streamlit 🎨</b>
</p>

<p align="center">
  <i>Making GATE PYQ preparation smarter with AI.</i>
</p>
