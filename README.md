# <p align="center">Osho chatbot Rag implementation sample </p>

## Overview
This project aims to create an AI-powered chatbot that mimics the conversational style and philosophical teachings of Osho, a renowned spiritual leader. By leveraging Retrieval-Augmented Generation (RAG), the chatbot provides contextually accurate responses derived from Osho's books and teachings stored as a knowledge base.


# Dataset 
The dataset is sourced by scraping the comprehensive collection of Osho's books available at https://www.alaalsayid.com/ebooks/OSHO%20pdf/.
These PDFs are preprocessed to extract clean, structured text suitable for embedding generation and efficient retrieval.

## ✨ Features  

**Knowledge Base Construction:**
Text from the books is converted into embeddings using a vectorizer (e.g., Sentence Transformers).
A vector database is employed to store the embeddings, enabling rapid retrieval of context-relevant information.

**Retrieval-Augmented Generation (RAG):**
Combines retrieval and generation to ground chatbot responses in Osho’s teachings.
The model first retrieves relevant excerpts from the vector database and incorporates them into dynamically generated responses, ensuring both relevance and coherence.

**Backend Development:**
Built using FastAPI, providing RESTful APIs for:
Querying the chatbot.
Retrieving contextual excerpts.


**Frontend Interface:**
A React-based user interface designed for an immersive and interactive experience.
Includes features such as real-time chat, conversation history, and accessibility enhancements.

**Persistent Conversation History:**
Chat history is stored and reused to maintain conversational continuity.
Users can revisit previous interactions for reference.

-
## 🚀 Getting Started  

### Open Using Daytona  

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).  
2. **Create the Workspace**:  
   ```  
   daytona create https://github.com/daytonaio/sample-python-rag-chatbot.git

   ```  

3. **Set up the environment variables by creating a ```.env``` file in the backend directory and add given details:**: 
   ```  
   GROQ_API_KEY=<YOUR_GROQ_API_KEY>
   ```  

4. **Start the Application**:  
   Navigate to backend folder 
      ```
      poetry run uvicorn src.app:app --reload
      ```  
   Navigate to frontend folder 
      ```
      npm start
      ```  

## Technologies Used

- **Daytona**: Development environment manager.  
- **React**: Frontend library for building user interfaces.    
- **Groq API**: Fast AI interface.
- **fastapi**: For restful API.  
- 
