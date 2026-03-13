from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse
import shutil

from fraud_model import predict_scammer
from chat_detector import detect_scam_message
from trust_score import calculate_trust_score
from scraper import get_binance_ads
from chatbot import p2p_chatbot
from screenshot_detector import analyze_screenshot
from blacklist import check_blacklist

app = FastAPI(
    title="Binance P2P Guardian AI",
    description="AI assistant to make Binance P2P safer and smarter",
    version="0.1.0"
)

# Redirect root to docs
@app.get("/")
def home():
    return RedirectResponse(url="/docs")


# Scam message detection
@app.get("/check_message", summary="Check Message")
def check_message(message: str):
    risk = detect_scam_message(message)
    return {"risk": risk}


# Trader risk prediction
@app.get("/check_trader", summary="Check Trader")
def check_trader(
    completion_rate: int,
    cancel_rate: int,
    account_age: int,
    disputes: int
):
    risk = predict_scammer(
        completion_rate,
        cancel_rate,
        account_age,
        disputes
    )
    return {"risk": risk}


# Trust score calculation
@app.get("/trust_score", summary="Trust Score")
def trust_score(
    completion_rate: int,
    cancel_rate: int,
    account_age: int,
    disputes: int,
    volume: int
):
    score = calculate_trust_score(
        completion_rate,
        cancel_rate,
        account_age,
        disputes,
        volume
    )
    return {"trust_score": score}


# Binance P2P ads
@app.get("/binance_ads", summary="Binance Ads")
def binance_ads():
    ads = get_binance_ads()
    return {"ads": ads}


# Simple AI chatbot
@app.get("/chatbot", summary="Chatbot")
def chatbot(question: str):
    answer = p2p_chatbot(question)
    return {"answer": answer}


# Screenshot scam detection
@app.post("/scan_screenshot", summary="Scan Screenshot")
async def scan_screenshot(file: UploadFile = File(...)):
    path = "temp.png"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_screenshot(path)
    return result


# Check blacklist
@app.get("/check_blacklist", summary="Check Blacklist")
def check_blacklist_api(trader_id: str):
    blacklisted = check_blacklist(trader_id)
    return {"blacklisted": blacklisted}
