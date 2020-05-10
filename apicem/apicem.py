import requests
import json
import urllib3
from pprint import pprint
from tabulate import *
def menu():

    print("APIC-EM services:\n")
    print("1) Host inventory")
    print("2) Devices List")
    print("3) Geolocate IP")
    print("4) Get devices configurations in files")
    print("0) Salir")
    
    while True:
        try:
            option = int(input("Elige una opcion:"))
            if option == 0:
                break
            elif option == 1:
                create_host_inventory()
                menu()
                break
            elif option == 2:
                print_devices()
                menu()
                break
            elif option == 3:
                geolocate()
                menu()
                break
            elif option == 4:
                get_devices_config()
                menu()
                break
            else:
                print("Elige una opcion entre 0 y 4.")
                menu()
        except ValueError:
            print("Elige una opcion entre 0 y 4")
    exit

def getticket():
    requests.packages.urllib3.disable_warnings()
    api_url = "https://SandBoxAPICEM.cisco.com/api/v1/ticket"
    headers = {
        "Content-Type":"application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
    }
    resp = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    resp_json = resp.json()
    return resp_json['response']['serviceTicket']

def create_host_inventory():
    api_url = "https://SandBoxAPICEM.cisco.com/api/v1/host"
    ticket = getticket()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    resp_json = resp.json()
    tableHeader = [
        "Number",
        "IP",
        "MAC",
        "Type"
    ]
    hostList = []
    counter = 0
    for item in resp_json['response']:
        counter += 1
        host = [
            counter,
            item['hostIp'],
            item['hostMac'],
            item['hostType']            
        ]
        hostList.append(host)
    print(tabulate(hostList,tableHeader))
    print("---------------------------------------------------------------------------------\n")

def print_devices():
    api_url = "https://SandBoxAPICEM.cisco.com/api/v1/network-device"
    ticket = getticket()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    resp_json = resp.json()
    pprint(resp_json)
    tableHeader = [
        "Number",
        "IP",
        "MAC",
        "Hostanme"
    ]
    hostList = []
    counter = 0
    for item in resp_json['response']:
        counter += 1
        host = [
            counter,
            item['managementIpAddress'],
            item['macAddress'],
            item['hostname']            
        ]
        hostList.append(host)
    print(tabulate(hostList,tableHeader))
    print("---------------------------------------------------------------------------------\n")

def geolocate():
    api_url = "https://sandboxapicem.cisco.com/api/v1/ipgeo/"
    ticket = getticket()

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": ticket
    }
    x = str(input("Introduce la IP que quieres geolocalizar: "))
    api_url = api_url + x
    resp = requests.get(api_url,headers=headers,verify=False)
    resp_json = resp.json()
    
    print("IP City: ",resp_json['response'][x]['city'])
    print("IP contient: ",resp_json['response'][x]['continent'])
    print("IP Country: ",resp_json['response'][x]['country'])
    print("---------------------------------------------------------------------------------\n")

def get_devices_config():
    api_url = "https://SandBoxAPICEM.cisco.com/api/v1/network-device/config"
    ticket = getticket()
    headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": ticket
    }
    
    resp = requests.get(api_url,headers=headers,verify=False)
    resp_json = resp.json()
    
    pprint(resp_json)
    for item in resp_json['response']:
        file1 = open(item['id'],"w+")
        file1.write(item['runningConfig'])

menu()
