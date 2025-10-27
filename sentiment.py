from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
system_rol = '''Pretend that you are a sentiment analyzer.
                 I give you feelings and you analyze the sentiment of the messages
                 and give me a response with an emoji included of the sentiment in question.'''

messages = [{"role": "system", "content": system_rol}]

class sentiment_analyzer:
    def __init__(self,input):
        self.input = input

    def analyze(self):
       # Add the user's text to the conversation
        messages.append({"role": "user", "content": self.input})

        #  Send the request to the model
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages
        )

        #  Get the assistant's response
        analyze = response.choices[0].message.content

        # Clear the conversation if you want to reset it each time
        messages.pop() 

        return "\x1b[1;32m" + analyze

if __name__ == "__main__":
    while True:
       text = input("\033[1;34m Enter a message to analyze: \033[0m ")
       stance = sentiment_analyzer(text).analyze()
       print(stance)
    





