# ProvectusInternship_GrigorGrigoryan

# 🎤 Concert Tour Info Service (2025–2026)

This Python service intelligently manages and retrieves information from domain-specific documents related to upcoming **concert tours in 2025–2026**. It uses **Retrieval Augmented Generation (RAG)** to ground its responses strictly in the ingested documents, ensuring reliable and relevant answers.

---

## 🚀 Objective

Build a lightweight, document-driven assistant that:
- Ingests user-uploaded concert tour documents
- Summarizes and indexes relevant content
- Answers user queries using only the ingested data

---

## 🧠 Core Functionalities

### 1. 📄 Document Ingestion

**User Input:**  
A plain-text document about concert tours.

**Processing Pipeline:**
- **Document Validation:** Checks if the content is about concerts, tours, performers, venues, etc.
- **Domain Filtering:** Rejects irrelevant content with a friendly message.
- **Summarization:** Produces a concise summary of valid documents.
- **Ingestion:** Adds the summary to the RAG system.
- **Feedback:** Returns a confirmation and the summary to the user.

**Example:**


User: Please, add this document to your database: [document contents] Service: Thank you for sharing! Your document has been successfully added to the database. Here is a brief summary of the data from the document: [summary]



---

### 2. ❓ Question Answering

**User Input:**  
A query about concert tours (e.g., performer schedules, venues, etc.).

**Processing Pipeline:**
- Uses RAG to search the document database.
- Retrieves relevant info and constructs an accurate response.
- All responses are strictly based on ingested documents.

**Example:**


User: Where is Lady Gaga planning to give concerts during autumn 2025? Service: She plans to go to [list of cities and additional details].



---

### (Optional) 🖥️ User Interface

A **Streamlit UI** can be added for improved interaction.

Suggested Features:
- Input box for adding documents or asking questions
- Response display in a clean format

---

## 📁 Project Structure

```bash
ProvectusInternship_GrigorGrigoryan
│   app.py                  # Streamlit app (optional UI)
│   main.py                 
│   README.md
│   requirements.txt
├───config
│   └── settings.py         # Configuration variables
├───data
│   └── documents/          # Folder for ingested text files
│       └── sample_doc.txt
├───ingestion
│   ├── document_checker.py # Validates if a document is about conccerts
│   ├── ingestor.py         # Ingests validated docs into the system
│   └── summarizer.py       # Summarizes relevant content
├───retrieval
│   ├── rag_qa.py           # RAG-based question answering logic
│   └── vector_store.py     # Handles embedding and document retrieval

```

---

## 📦 Setup & Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/grig001/ProvectusInternship_GrigorGrigoryan.git
   cd ProvectusInternship_GrigorGrigoryan
   ```
   
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the main script**
    ```bash
    python main.py
    ```

4. **(Optional) Launch Streamlit UI**
    ```bash
    streamlit run app.py
    ```


## 📝 Requirements

Dependencies are listed in `requirements.txt`, including:

- `transformers`
- `onnxruntime-gpu==1.17.1`
- `streamlit`
- `chromadb`

---

## 📬 Future Improvements

- Add support for non-text formats (e.g., PDFs)
- Improve summarization with LLM fine-tuning
- Include admin control to delete or update documents
- Log user queries for analytics and feedback
- **Implement an additional mode to enhance the bot’s usefulness:**  
  If a user does not upload a document but provides a musician or band name, the bot should:
  - Perform an online search (e.g., via SerpAPI, Bing API, or another search engine wrapper)
  - Retrieve details about the artist’s upcoming concerts from publicly available sources
  - Generate and return an answer based on this search result.


   
