import openai

def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    
open_api_key = open_file('api_key.txt')

def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
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
    prompt = 'Write an AI project idea: '
    response = gpt3_completion(prompt)
    print(response)