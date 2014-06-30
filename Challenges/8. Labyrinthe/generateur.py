import random

links = ["5862"]	# links comporte la liste des liens du labyrinthe (Commence a 5862)
i = 0
while i <= 100:	# nombre de fichier a créer
	ok = True	
	link = str(random.randint(1000,9999));	# genere un lien

	for l in links:
		if l == link:
			ok = False	# on vérifie que le lien que l'on vien de tirer n'a pas déjà été tiré (sinon on recommence la boucle while)
	if ok :
		links.append(link)	# ajoute le lien à la liste des lien déjà tiré
		fichier = open("links/" + str(links[len(links)-2]) + ".html", "w")	# on ouvre un fichier portant le nom de notre lien tiré précedement...
		fichier.write("Vous devriez essayer le code <b>" + link + "</b>");	# ... et on y écrit le lien que l'on vien de tiré
		fichier.close()	# on ferme correctement notre fichier
		i+=1;	# ajoute 1 a notre nombre de fichier

fichier = open("links/" + link + ".html", "w")	# on ouvre un dernier fichier...
fichier.write("Vous devriez essayer le code <b>" + str(links[0]) + "</b> Le secret est Marmite");	# ... et on ferme le labyrinthe en ajoutant le secret
fichier.close()	# on ferme correctement notre fichier