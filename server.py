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
        f = open('cuentas.txt', 'r')
        data = json.loads(f.read())
        for key,value in data.items():
            print(text)
            if key == text:
                self.wfile.write(str(value).encode('ascii'))
        f.close()

    def do_GET(self):
        '''Callback para GETs'''
        nombre = self.path.split("name=",1)
        try:
            usuario = nombre[1]
            self.get_File(usuario)
        except IndexError:
            pass



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