import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site pudim não está acessível no momento')
else:
    print('consegui acessar o site com sucesso!')
    print(site.read())