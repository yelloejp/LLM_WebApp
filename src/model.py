import ollama
def llm_response(model :str, prompt :str):
    response = ollama.chat(
        model= model, 
        messages=[
            {
                'role':'user',
                'content': prompt,
            },
        ]
    )
    
    return response['message']['content']
