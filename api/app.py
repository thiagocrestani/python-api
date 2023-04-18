from fastapi import FastAPI
from api.resources import router
from api.database import init_db, db_session
import uvicorn

app = FastAPI()

# Define a função para inicializar o banco de dados
async def startup():
    init_db()

# Adiciona o evento de inicialização do banco de dados à aplicação
app.add_event_handler("startup", startup)

# Adiciona o roteador na API
app.include_router(router)

# Encerramento da conexão com o banco de dados após cada requisição
@app.middleware("http")
async def db_session_middleware(request, call_next):
    response = None
    try:
        # Cria uma sessão para a requisição atual
        request.state.db = db_session()
        response = await call_next(request)
    finally:
        # Encerra a sessão após a requisição ser processada
        request.state.db.close()
    return response

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)