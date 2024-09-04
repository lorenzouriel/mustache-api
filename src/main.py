from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configura o Jinja2 para renderizar templates Mustache
templates = Jinja2Templates(directory="templates")

@app.post("/send-message")
async def send_message(request: Request):
    # Obtém os dados do JSON da requisição
    data = await request.json()
    nome = data.get('nome')
    quantidade = data.get('quantidade')

    # Renderiza o template Mustache com os dados fornecidos
    message = templates.get_template('message.mustache').render(nome=nome, quantidade=quantidade)

    # Aqui você poderia enviar a mensagem para um serviço de email/SMS/etc.
    print('Mensagem gerada:', message)

    return JSONResponse(content={
        'status': 'Mensagem enviada com sucesso!',
        'mensagem': message
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)