from fastapi import FastAPI, UploadFile, File
import shutil

from fraud_model import predict_scammer
from chat_detector import detect_scam_message
from trust_score import calculate_trust_score
from scraper import get_binance_ads
from chatbot import p2p_chatbot
from screenshot_detector import analyze_screenshot
from blacklist import check_blacklist

app=FastAPI(title="Binance P2P Guardian AI")

@app.get("/")
def home():

    return {"message":"Binance P2P Guardian Running"}

@app.get("/check_message")
def check_message(message:str):

    return {"risk":detect_scam_message(message)}

@app.get("/check_trader")
def check_trader(
completion_rate:int,
cancel_rate:int,
account_age:int,
disputes:int
):

    risk=predict_scammer(
    completion_rate,
    cancel_rate,
    account_age,
    disputes
    )

    return {"risk":risk}

@app.get("/trust_score")
def trust_score(
completion_rate:int,
cancel_rate:int,
account_age:int,
disputes:int,
volume:int
):

    score=calculate_trust_score(
    completion_rate,
    cancel_rate,
    account_age,
    disputes,
    volume
    )

    return {"trust_score":score}

@app.get("/binance_ads")
def binance_ads():

    return {"ads":get_binance_ads()}

@app.get("/chatbot")
def chatbot(question:str):

    return {"answer":p2p_chatbot(question)}

@app.post("/scan_screenshot")
async def scan_screenshot(file:UploadFile=File(...)):

    path="temp.png"

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return analyze_screenshot(path)

@app.get("/check_blacklist")
def check_blacklist_api(trader_id:str):

    return {"blacklisted":check_blacklist(trader_id)}