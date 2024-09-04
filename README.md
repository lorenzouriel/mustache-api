# API de Mensageria com Mustache e FastAPI

Este projeto demonstra como criar uma API de mensageria baseada em Mustache usando FastAPI. A API permite enviar mensagens formatadas com Mustache com base em dados fornecidos na requisição.

## Estrutura do Projeto
```
project-root/
├── templates/
│   └── message.mustache
├── src/
│   └── main.py
└── requirements.txt
```

## Instalação
1. Clone este repositório ou baixe o código.
```git
git clone https://github.com/lorenzouriel/mustache-api.git
```

2. Instale as dependências:
```bash
pip install fastapi jinja2 uvicorn
```

## Estrutura dos Arquivos
`templates/message.mustache`

Este arquivo contém o template de mensagem. Exemplo:
```mustache
Olá {{nome}},

Você tem {{quantidade}} novas mensagens em sua caixa de entrada.

Obrigado,
Equipe de Suporte
```

`src\main.py`

Este é o arquivo principal da aplicação FastAPI:
```python
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
```

## Execução
Para executar a aplicação, use o comando:
```
uvicorn main:app --reload
```

### Exemplos de Uso
Para enviar uma mensagem, faça uma requisição POST para /send-message com um corpo JSON, como o exemplo abaixo:
```bash
curl -X POST http://localhost:8000/send-message \
-H "Content-Type: application/json" \
-d '{"nome": "Lorenzo", "quantidade": 5}'
```

### Resposta Esperada
```json
{
  "status": "Mensagem enviada com sucesso!",
  "mensagem": "Olá Lorenzo,\n\nVocê tem 5 novas mensagens em sua caixa de entrada.\n\nObrigado,\nEquipe de Suporte"
}
```