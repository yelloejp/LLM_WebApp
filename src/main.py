from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from src.model import llm_response

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get('/')
def read_form():
    return 'hello world'

@app.get('/form')
def form_post(request: Request):
    result = ' '
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, task: str = Form(), prompt: str = Form()):
    if task == "llama2":
            model = "llama2"
    else:
        model = "llama3"

    result = llm_response(model, prompt)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result, 'task': task})


