from openai import OpenAI

client = OpenAI(api_key="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")

chat_log = []

while True:
    user_message = input("Enter input: ")
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )

        assistant_response = response.choices[0].message.content
        print("ChatGPT: ", assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
