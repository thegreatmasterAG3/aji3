import openai

def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=stext,
            temperature=0.5,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
    )
    content = response.choices[0].text.strip()
    return content

while True:
    print("")
    query = input("You : ")
    response = gpt3(query)
    print("")
    print("Aji3 : ",response)
