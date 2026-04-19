import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Check if Gemini API key exists, otherwise we'll return mock AI responses to prevent crashing
API_KEY = os.getenv("GEMINI_API_KEY")

try:
    if API_KEY:
        client = genai.Client(api_key=API_KEY)
    else:
        client = None
except Exception:
    client = None

def navigate_prompt(destination: str, mock_data: dict) -> str:
    """Uses Gemini to suggest the best route based on mock crowd data."""
    if not client:
        return f"AI Simulation: To reach {destination}, use Gate 2. It has low crowd levels right now."
        
    prompt = f"""
    User wants to go to {destination}. 
    Here is the current crowd data for available routes:
    {mock_data}
    
    Act as a smart assistant. Suggest the best route to take, explaining why (least crowded).
    Keep it concise and helpful. Use balancing if both are low.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"

def ask_ai_prompt(user_question: str, queue_data: list, crowd_data: dict) -> str:
    """General AI Assistant based on current data."""
    if not client:
         return "AI Simulation: I recommend Stall B. It only has a 5 min wait time compared to others."
         
    prompt = f"""
    You are 'AI CrowdSense', a smart assistant at a large stadium event.
    User asks: "{user_question}"
    
    Current queue data: {queue_data}
    Current crowd data: {crowd_data}
    
    Answer naturally and helpfully. Suggest the best option to minimize waiting and balance the crowd. Keep it under 2 sentences.
    """
    
    try:
         response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
         return response.text
    except Exception as e:
         return f"Error connecting to AI: {str(e)}"
