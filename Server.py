import soaplib
from soaplib.core.service import rpc, DefinitionBase
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from soaplib.core.service import soap

from subprocess import check_output


class CalculationService(DefinitionBase):
    @soap(String,_returns=Array(String))
    def call_math_function(self,number):
        rezults = check_output(["C:\Users\Shakirov Farit\Desktop\math_function.exe", number]).split('\r\n')
        rezults.pop()
        return rezults

if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([CalculationService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 7777, wsgi_application)
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"

