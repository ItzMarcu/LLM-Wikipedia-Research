from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv
import requests
import os

app = FastAPI(title="Wikipedia API")
origins = ["https://itzmarcu.github.io"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
client = Groq(api_key=os.getenv("API_KEY"))

URL: str = "https://it.wikipedia.org/wiki/"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    }

# === ROUTES PRINCIPALI === 
@app.get("/")
def home(): 
    return {"status-code": 200}

@app.get("/q")
def query(parametro: str = None): 
    if not parametro: 
        raise HTTPException(status_code=400, detail="missing query parameters")
    
    query_url = f"{URL}{parametro}"
    try: 
        response = requests.get(query_url, headers=headers, timeout=15)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.find(id="mw-content-text").text
            
            if not text: 
                raise HTTPException(status_code=404, details="data not found!")
            
            return analyze_text(text[:10000])
        
        return {"errore": f"status-code: {response.status_code}"}
    except requests.RequestException as e: 
        return {"exception": f"{e}"}


# === ANALISI LLM ===
def analyze_text(text: str = None):
    if not text:
        return {"exception": Exception("Errore nell'analisi del testo")}

    inner_message = [
        {
            "role": "user",
            "content": f"Analizza questo testo da wikipedia e dammi qualcosa di facilmente leggibile, dai soltanto il testo utile niente convenevoli: {text}"
        }
    ]

    try: 
        completion = client.chat.completions.create(
            messages=inner_message,
            model="llama-3.3-70b-versatile"
        )
        return completion.choices[0].message.content
    
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"errore alla riga 73 {str(e)}")