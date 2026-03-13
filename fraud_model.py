import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH="models/fraud_model.pkl"

def train_model():

    data={
    "completion_rate":[99,98,97,95,90,70,60,40],
    "cancel_rate":[1,1,2,3,5,20,30,40],
    "account_age":[800,700,600,500,300,100,60,10],
    "disputes":[0,0,1,1,2,4,5,8],
    "scam":[0,0,0,0,0,1,1,1]
    }

    df=pd.DataFrame(data)

    X=df[["completion_rate","cancel_rate","account_age","disputes"]]
    y=df["scam"]

    model=RandomForestClassifier()
    model.fit(X,y)

    os.makedirs("models",exist_ok=True)
    joblib.dump(model,MODEL_PATH)

def load_model():

    if not os.path.exists(MODEL_PATH):
        train_model()

    return joblib.load(MODEL_PATH)

model=load_model()

def predict_scammer(completion_rate,cancel_rate,account_age,disputes):

    prediction=model.predict([[completion_rate,cancel_rate,account_age,disputes]])

    if prediction[0]==1:
        return "High Risk"
    else:
        return "Low Risk"