#!/usr/bin/env python3

""" fonction de vérification de l'hote """

import requests
import socket

def check_localhost():
	""" tester l'host de la variable """
	localhost = socket.gethostbyname('localhost')

	if localhost == '127.0.0.1':
		return True
	else:
		print("ERROR!!")

print(check_localhost())

def check_connectivity():
	""" Ping sur un site """

	request = requests.get("http://www.google.com") #renvoie un code d'etat du site

	if request.status_code == 200:
		return True
	else:
		print("Don't send status code 200")
	#return request

print(check_connectivity())