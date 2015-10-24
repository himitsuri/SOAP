from suds.client import Client
calculation_client = Client('http://localhost:7777/?wsdl')
result = calculation_client.service.call_math_function("-4.8")
print result
