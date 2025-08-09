from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY


llm = ChatGroq(
    groq_api_key = GROQ_API_KEY,
    model_name = "llama-3.3-70b-versatile",
    temperature=0.3
)


itnineary_prompt = ChatPromptTemplate([
    ("system" , "You are an expert travel assistant specializing in personalized day trip planning. Design a concise, bulleted itinerary for a day trip in {city} tailored to the user's interests: {interests}. Include 4-6 activities with brief descriptions, estimated times, and practical details (e.g., addresses or transportation tips). Ensure the itinerary is well-balanced, considering the user's interests and the city's unique offerings."),
    ("human" , "Create a itineary for my day trip")
])

def generate_itineary(city:str , interests:list[str]) -> str:
    response = llm.invoke(
        itnineary_prompt.format_messages(city=city,interests=', '.join(interests))
    )

    return response.content