import random

links = ['Le secret est "marmites"']
i = 0
while i <= 442:
	ok = True
	link = random.randint(1000,9999);

	for l in links:
		if l == link:
			ok = False
	if ok :
		links.append(link)
		fichier = open("links/" + str(link) + ".txt", "w")
		fichier.write("Vous devriez essayer le code <b>" + str(links[len(links)-2]) + "</b>");
		fichier.close()
		i+=1;
