import openai

def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    
openai.api_key = open_file('api_key.txt')

def gpt3_completion(prompt, engine='text-davinci-002', temp=1, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['USER:', 'MEKABOT:']):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    try: 
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen,
            stop=stop)
        text = response['choices'][0]['text'].strip()
        return text
    except Exception as e:
        return f'This is your error: ==> {e}'

    

if __name__ == '__main__':
    conversation = list()
    converse = True
    
    # Creating an open ended chat with while loop
    while converse:
        # Get user's PROMPT
        user_input = input('USER: ')
        if user_input.lower() == 'end':
            converse = False
        else:
            # Add to the conversation list for display
            conversation.append(f"USER: {user_input}")
            # Format display 
            text_block = '\n'.join(conversation)
            # Setting prompt to info for the machine to work on
            prompt = open_file('market_prompt.txt').replace('<<BLOCK>>', text_block)
            # Set bot conversation prompt
            prompt = prompt + '\nMEKABOT:'
            # Calling the completions endpoint and passing the prompt
            response = gpt3_completion(prompt)
            # Display on screen
            print('MEKABOT:', response)
            # Adding bots response to conversation list
            conversation.append(f"MEKABOT: {response}")