from rag_engine import retrieve_docs
from llm import generate_answer
from analytics import calculate_answer
from prediction import predict_profit
from intent import detect_intent


def handle_query(query):
    intent = detect_intent(query)

    if intent == "calculation":
        result = calculate_answer(query)
        if result:
            return result

    elif intent == "prediction":
        return predict_profit()

    docs = retrieve_docs(query)
    return generate_answer(query, docs)


# CLI chatbot
if __name__ == "__main__":
    print("💰 AI Financial Assistant (type 'exit' to quit)\n")

    while True:
        q = input("You: ")

        if q.lower() == "exit":
            break

        print("Bot:", handle_query(q))
        print("-" * 50)