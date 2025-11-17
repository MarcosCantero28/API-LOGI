from waitress import serve
from api import app
import sys

if __name__ == '__main__':
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    
    print("Servidor iniciado en http://127.0.0.1:8000", flush=True)
    serve(app, host='127.0.0.1', port=8000, _quiet=False)