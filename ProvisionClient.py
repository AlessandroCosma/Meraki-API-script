#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    File name: ProvisionClient.py
    Author: Cosma Alessandro
    Date created: 05/03/2020
    Date last modified: 06/03/2020
    Python Version: 3.7
"""


from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.models.provision_network_clients_model import ProvisionNetworkClientsModel
from meraki_sdk.exceptions.api_exception import APIException


def request_params():
    api_key = input("Insert API KEY: ")
    network_id = input("Insert NETWORK ID: ")
    file_name = input("Insert config file name: ")
    device_policy = input("Insert group policy name: ")
    group_policy_id = input("Insert policy ID: ")

    return(api_key, network_id, file_name, device_policy, group_policy_id)


def install_configuration(api_key, network_id, file_name, device_policy, group_policy_id):

    # define meraki sdk client
    meraki = MerakiSdkClient(api_key)


    number_of_clients = 0
    # define total number clients
    with open(file_name+'.txt') as f:
       number_of_clients = sum(1 for _ in f)

    # This is a list of dict. Each dict contains client's info
    dictlist = [{} for i in range(0,number_of_clients)]

    # open file with the config [format = mac;name ]
    f = open(file_name+'.txt', 'r')

    for i in range (0,number_of_clients):
        # create an object of type "ProvisionNetworkClientsModel"
        client = ProvisionNetworkClientsModel()
        # read each line at each iteration
        line = f.readline()
        line_splitted = line.split(";")

        dictlist[i]["network_id"] = network_id
        # Populate client info
        client.mac = line_splitted[0].rstrip("\n")
        client.name = line_splitted[1].rstrip("\n")
        client.device_policy = device_policy
        client.group_policy_id = group_policy_id
        dictlist[i]["provision_network_clients"] = client

    for i in range (0,number_of_clients):
        try:
            result = meraki.clients.provision_network_clients(dictlist[i])

        except APIException as e:
            print(e)

    # close file
    f.close()


def main():

    proceed = False

    while not proceed:
        # request params
        (api_key, network_id, file_name, device_policy, group_policy_id) = request_params()

        correct = False
        while not correct:
            risp = input("Continue?(s/n)  ")
            if risp == "s":
                proceed = True
                correct = True
            elif risp == "n":
                #proceed = False
                correct = True
            else:
                print("Character not valid!")

    install_configuration(api_key, network_id, file_name, device_policy, group_policy_id)

if __name__ == "__main__":
    main()
