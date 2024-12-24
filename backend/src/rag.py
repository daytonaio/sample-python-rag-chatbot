from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_groq import ChatGroq
from operator import itemgetter

from decouple import config
from src.qdrant import vector_store

# Load the GROQ API key
groq_api_key = config("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Please ensure it is added to your .env file or environment variables.")

# Initialize the ChatGroq LLM
model = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,       # Example parameter
    max_tokens=500,      # Adjust token limit as needed
    timeout=60,          # Optional timeout in seconds
    max_retries=2,       # Number of retries in case of failure
    api_key=groq_api_key # Pass the API key
)
# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)

prompt_template = """
Answer the question based on the context, in a concise manner, in markdown and using bullet points where applicable.

Context: {context}
Question: {question}
Answer:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

retriever = vector_store.as_retriever()

def create_chain():
    chain = (
        {
            "context": retriever.with_config(top_k=4),
            "question": RunnablePassthrough(),
        }
        | RunnableParallel({
            "response": prompt | model,
            "context": itemgetter("context"),
            })
    )
    return chain

def get_answer_and_docs(question: str):
    chain = create_chain()
    response = chain.invoke(question)
    answer = response["response"].content
    context = response["context"]
    return {
        "answer": answer
    }



