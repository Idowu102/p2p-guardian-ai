def calculate_trust_score(completion_rate,cancel_rate,account_age,disputes,volume):

    score=0

    score+=completion_rate*0.35
    score+=(100-cancel_rate)*0.2
    score+=min(account_age/365,1)*20
    score+=volume*0.1
    score-=disputes*6

    score=max(min(score,100),0)

    return round(score,2)