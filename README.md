# 🧩 Chunking Visualizer

An interactive web app to **visualize and understand text chunking** strategies used in NLP and Retrieval-Augmented Generation (RAG).  

🔗 **Live Demo:** [Chunking Visualizer](https://chunking-visualizer.onrender.com/)

---

## 🚀 Features
- Paste any text and split it into chunks.
- Choose different **splitter strategies**:
  - Character Splitter  
  - Recursive Splitter (Python / JS / Markdown)  
- Adjust **chunk size** and **overlap** dynamically.  
- See text highlighted with unique colors per chunk.  
- Overlapping chunks are blended with new colors for better understanding.  

---

## 📸 Screenshot

![App Screenshot 1]([assets/screenshot1.png](https://github.com/Akshay9715/Chunk-Visualizer/blob/main/assests/screenshot1.png))
![App Screenshot 2]([assets/screenshot2.png](https://github.com/Akshay9715/Chunk-Visualizer/blob/main/assests/screenshot2.png))

---

## 🛠️ Tech Stack
- **Backend:** Flask + LangChain  
- **Frontend:** HTML + CSS + Jinja templates  
- **Deployment:** Render  
- **Containerization:** Docker  

---

## 🐳 Run Locally with Docker
Clone the repository and run:

```bash
git clone https://github.com/<your-username>/chunking.git
cd chunking
```
Build the image:

```bash
docker build -t chunking:latest .
```

Run the container:

```bash
docker run -p 5000:8080 chunking
```

App will be available at: http://localhost:5000

📦 Installation (Without Docker)

```bash
git clone https://github.com/<your-username>/chunking.git
cd chunking
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```

📖 About

Chunking is the process of splitting large text into smaller pieces so they can be processed efficiently by language models.
This app helps visualize how chunking works, and why chunk size + overlap matter for efficiency and semantic coherence.

👨‍💻 Author

Made with ❤️ by Akshay Choudhary
