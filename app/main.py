import uvicorn
from config.server import createServer

server = createServer() 

if __name__ == '__main__':
    uvicorn.run("main:server", host='127.0.0.1', port=8080, log_level="debug", reload=True)
