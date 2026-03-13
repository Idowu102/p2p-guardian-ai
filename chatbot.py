def p2p_chatbot(question):

    q=question.lower()

    if "safe" in q:
        return "Always trade inside Binance P2P and verify payment before releasing crypto."

    if "scam" in q:
        return "Avoid traders asking to move to WhatsApp or Telegram."

    return "Use P2P Guardian AI to analyze traders."