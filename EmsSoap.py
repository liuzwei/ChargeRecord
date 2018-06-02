import zeep

if __name__ == '__main__':
    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    print(client.service.Method1('AA', "asd"))