import os
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
from llama_index import SimpleDirectoryReader
from dotenv import load_dotenv


load_dotenv()

def load_data():
    reader = SimpleDirectoryReader(input_dir="./data")
    docs = reader.load_data()
    service_context = ServiceContext.from_defaults(
                            llm=OpenAI(model="gpt-4",
                            temperature=0.5,
                            system_prompt=os.environ.get("SYSTEM_PROMPT")
                        ))
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    return index

def create_answer(prompt):
    index = load_data()
    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
    response = chat_engine.chat(prompt)
    return response
