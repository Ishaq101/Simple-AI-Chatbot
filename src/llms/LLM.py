import os
from dotenv import load_dotenv
load_dotenv() 
from langchain_google_genai import ChatGoogleGenerativeAI


#######
# LLM 
#######

model_gemini = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    disable_streaming=False,
    # callbacks=[callback],
    verbose=True)
