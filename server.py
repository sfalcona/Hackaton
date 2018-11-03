import http.server
import socketserver
import simplejson
import json
import random
import os

def jsonPPrint(filename):
    f = open(filename, 'r')
    data = json.loads(f.read())
    print(json.dumps(data, indent=4, sort_keys=True))


class S(http.server.BaseHTTPRequestHandler):
    '''Servidor HTTP'''

    def get_File(self, text):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Text es el nombre del usuario que quiero leer
        with open('cuentas.txt', 'r') as f:
            data = json.loads(f.read())
            for key,value in data.items():
                if key == text:
                    self.wfile.write(str(value).encode('ascii'))


    def do_GET(self):
        '''Callback para GETs'''
        nombre = self.path.split("name=",1)
        try:
            usuario = nombre[1]
            self.get_File(usuario)
        except IndexError:
            pass

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        recibo = self.data_string.decode("utf-8")
        datos = recibo.rsplit('=')
        # Datos[0] es el nombre, datos[1] es el nuevo monto
        with open('cuentas.txt', 'r') as f:
            data = json.loads(f.read())
            for key,value in data.items():
                if key == datos[0]:
                    print(key + str(value))
                    data[key] = value - int(datos[1])
        
        with open('cuentas.txt', 'w') as f:
            json.dump(data, f)

        self.send_response(200)
        self.end_headers()

        

    def do_HEAD(self):
        self._set_headers()



def run(server_class=http.server.HTTPServer, handler_class=S, server='localhost', port=80):
    server_address = (server, port)
    httpd = server_class(server_address, handler_class)
    print('Server starting at ' + str(server_address[0]) + ':' + str(port))
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 3:
    run(server=argv[1], port=int(argv[2]))
    print(argv[1])
else:
    run()