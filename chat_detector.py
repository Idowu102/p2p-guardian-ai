SCAM_PHRASES=[
"send first",
"release later",
"outside platform",
"whatsapp trade",
"telegram deal"
]

def detect_scam_message(message):

    message=message.lower()
    score=0

    for phrase in SCAM_PHRASES:

        if phrase in message:
            score+=1

    if score>=2:
        return "High Risk Message"

    if score==1:
        return "Suspicious"

    return "Safe"