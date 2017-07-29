import os
import json

def check_input(prompt, arguments):

	check = False
	before_prompt = ""
	while not check:
		print("")
		entrer_clavier = str(input(before_prompt + prompt).lower())

		if entrer_clavier in arguments:
			check = True
		else:
			before_prompt = "Entrer l'un des mots suivant : {}\n".format(arguments)

def parties():
	parties = []

	with open('parties.json') as f:

		data = json.load(f)
		for partie in data:
			parties.append(partie['partie'])

		os.system('cls')
		i = 1
		while i < len(parties)+1:
			for partie in parties:
				print(i, ". Partie", partie['numero'],", de", partie['nom'])
				i+=1
				
			print(len(parties)+1, ". Nouvelle partie")
