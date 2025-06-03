from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

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
    # Bind to 0.0.0.0 so other devices on LAN can access
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Server running on http://192.168.56.1:8000/?wsdl")
    server.serve_forever()
