import requests
import json
import urllib3
from pprint import pprint
def menu():

    print("APIC-EM services:\n")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("0) Salir")
    
    while True:
        try:
            option = int(input("Elige una opcion:"))
            if option == 0:
                break
            elif option == 1:
                suma()
                break
            elif option == 2:
                resta()
                break
            elif option == 3:
                multi()
                break
            elif option == 4:
                divi()
                break
            else:
                print("Elige una opcion entre 0 y 4.")
                menu()
        except ValueError:
            print("Elige una opcion entre 0 y 4")
    exit

menu()
"""
requests.packages.urllib3.disable_warnings()
url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"

headers = {
    'Content-Type': 'application/json'
}
body_json = {
    'password': 'Xj3BDqbU',
    'username': 'devnetuser'
}

resp = requests.post(url, json.dumps(body_json),headers=headers,verify=False)

print("La peticion tiene el estado:",resp.status_code)
response_json = resp.json()

print("El ticket del servicio asignado es: ", response_json['response']['serviceTicket'])
pprint(response_json)

https://SandBoxAPICEM.cisco.com 

User: devnetuser
PW: Cisco123!"""