from model import chat

query = chat(
    system= "You are a helpful assistant",
    user= "How have you been?"
    )

print(query)
