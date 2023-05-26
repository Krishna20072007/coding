import wolframalpha

# Replace 'YOUR_API_KEY' with your actual API key from Wolfram Alpha
app_id = '2J73HU-6LVHEQE75Y'

def ask_wolfram(question):
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        answer = next(res.results).text
        print("Answer:", answer)
    except (wolframalpha.WolframAlphaError, StopIteration):
        print("Sorry, I couldn't find an answer to your question.")

# Example usage
question = input("Ask a question: ")
ask_wolfram(question)
