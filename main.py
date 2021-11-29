#Este modulo se encarga de correr la aplicacion, importa el modulo o instancia App
from src.app import app

HOST='localhost'
PORT=4000
DEBUG=True

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)