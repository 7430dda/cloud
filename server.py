from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import os

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f'Hello, {name}!'

app = Application(
    [HelloWorldService],
    'spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = int(os.environ.get("PORT", 8000))
    server = make_server('0.0.0.0', port, wsgi_app)
    print(f"Server running on http://0.0.0.0:{port}/?wsdl")
    server.serve_forever()
