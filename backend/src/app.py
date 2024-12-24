from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.rag import get_answer_and_docs
from src.qdrant import upload_website_to_collection
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(
    title='rag api',
    description = 'a simple rag api',
    version='0.1',
)
origins = [
    "http://localhost:3000",  # Local development
    "https://1bac81bb.oshogpt.pages.dev/"  # Deployed frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
)

class Question(BaseModel):
    message:str

@app.post('/chat')
def chat(message:Question):
    response = get_answer_and_docs(message.message)
   
    response_data={
        'question':message.message,
        'answer':response['answer']
    }
    return JSONResponse(content=response_data,status_code=200)

@app.post('/indexing')
def indexing(url:str):
    try:
        response = upload_website_to_collection(url)
        return JSONResponse(content=response,status_code=200)
    except Exception as e:
        return JSONResponse(content={'error':str(e)},status_code=400)


