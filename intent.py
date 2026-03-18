def detect_intent(query):
    query = query.lower()

    if "predict" in query or "future" in query:
        return "prediction"

    if "total" in query or "sum" in query or "profit" in query or "category" in query:
        return "calculation"

    return "rag"