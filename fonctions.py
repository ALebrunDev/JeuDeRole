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
