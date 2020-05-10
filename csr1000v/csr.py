from netmiko import ConnectHandler
import json
import requests
import urllib3
from pprint import pprint
from tabulate import *
def menu():

    print("CSR1000v:\n")
    print("1) Listado de interfaces")
    print("2) Crear interfaz")
    print("3) Borrar interfaz")
    print("4) Routing table")
    print("5) YANG module request 1. Restconf state")
    print("6) YANG module request 2. Get interface type")
    print("0) Salir")
    
    while True:
        try:
            option = int(input("Elige una opcion: "))
            if option == 0:
                break
            elif option == 1:
                int_list()
                menu()
                break
            elif option == 2:
                c_interface()
                menu()
                break
            elif option == 3:
                delete_int()
                menu()
                break
            elif option == 4:
                route_table()
                menu()
                break
            elif option == 5:
                yang1()
                menu()
                break
            elif option == 6:
                yang2()
                menu()
                break
            else:
                print("Elige una opcion entre 0 y 6.")
                menu()
        except ValueError:
            print("Elige una opcion entre 0 y 6")
    exit

def int_list():

    ssh = ConnectHandler(device_type='cisco_ios',host='192.168.56.101',port='22',username='cisco',password='cisco123!')
    output = ssh.send_command("sh ip interface brief")
    print("sh ip interfaces brief:\n{}".format(output))
   

def c_interface():
    requests.packages.urllib3.disable_warnings()
    url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback77"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basic_auth = ("cisco","cisco123!")

    body = {
    "ietf-interfaces:interface": {
                "name": "Loopback77",
                "description": "Prueba",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "77.77.77.77",
                            "netmask": "255.255.255.0"
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
    }


    resp = requests.put(url,data=json.dumps(body), auth=basic_auth, headers=headers, verify=False)

    print(resp.status_code) 

def delete_int():
    requests.packages.urllib3.disable_warnings()
    url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback77"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basic_auth = ("cisco","cisco123!")

    resp = requests.delete(url, auth=basic_auth, headers=headers, verify=False)
    

def route_table():

    requests.packages.urllib3.disable_warnings()
    url = "https://192.168.56.101/restconf/data/ietf-routing:routing-state"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basic_auth = ("cisco","cisco123!")

    resp = requests.get(url, auth=basic_auth, headers=headers, verify=False)
    resp_json = resp.json()

    routes = []
    counter = 0
    for item in resp_json['ietf-routing:routing-state']['routing-instance'][0]['ribs']['rib'][0]['routes']['route']:
        counter +=1
        route = [
            counter,
            item['destination-prefix'],
            item['next-hop']['outgoing-interface']
        ]
        routes.append(route)

    tableHeader= ["Number","Destination network","Outgoing interface"]
    print(tabulate(routes,tableHeader))


def yang1():

    requests.packages.urllib3.disable_warnings()
    url = "https://192.168.56.101/restconf/data/ietf-restconf-monitoring:restconf-state"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basic_auth = ("cisco","cisco123!")

    resp = requests.get(url, auth=basic_auth, headers=headers, verify=False)
    resp_json = resp.json()

    pprint(resp_json)

def yang2():

    x = str(input("Introduce la interfaz: "))
    requests.packages.urllib3.disable_warnings()
    url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface="+x+"/type"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basic_auth = ("cisco","cisco123!")

    resp = requests.get(url, auth=basic_auth, headers=headers, verify=False)
    resp_json = resp.json()

    pprint(resp_json)

menu()