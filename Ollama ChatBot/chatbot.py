import ollama
import json
llm_model = 'llama3.2:latest'
msg = []
while True:
    user_query = input("Enter your query: ")

    if user_query.lower()=='exit':
        print('Thank you, visit again :)')
        break

    msg.append({'role':'user','content':user_query})

   
    response = ollama.chat(
            llm_model,msg)

    bot_response = response['message']['content']

    print('Bot:',bot_response)

    msg.append({'role':'assistant','content':bot_response})


