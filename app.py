import streamlit as st
import google.generativeai as genai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set up Google GenAI API Key
os.environ["GOOGLE_API_KEY"] = "your_google_api_key"

# Initialize Google GenAI Model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Define prompt template for travel recommendations
prompt_template = PromptTemplate(
    input_variables=["source", "destination"],
    template="""
    You are an AI travel assistant. A user wants to travel from {source} to {destination}. 
    Provide travel options for cab, train, bus, and flight with estimated prices and travel times.
    """
)

# Create an LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit UI
st.title("AI-Powered Travel planner")


source = st.text_input("Enter Source Location")
destination = st.text_input("Enter Destination Location")


if st.button("Find Travel Options"):
    if source and destination:
        response = chain.run({"source":source,"destination":destination})
        st.write(response)
    else:
        st.warning("Please enter both source and destination")