import os
import openai
import config

openai.api_key = config.API_KEY
print("line3")
# prompt = "Can you recommend a good restaurant in New York City?"
count = 0
print("Hi! This is Tyler-bot")
a   = True
while a:
    if count == 0:
        print("\n")
        prompt = input("Ask me anything: ")
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        )

        # print("resp",response)

        print("Tyler-bot: ",response.choices[0].text.strip())
        count +=1
        print(count)
    elif count > 0:
        print("\n")
        prompt = input("Tyler: What else you wanna ask?\n")
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        )


        # print("resp",response)

        print("Tyler-bot",response.choices[0].text.strip())
        print("\n")
        further_que = input("Tyler-bot: Any other question for me? (Y/n): ")
        if further_que == "y" or further_que == "Y":
            a = True
        elif further_que == "n" or further_que == "N":
            a = False
        