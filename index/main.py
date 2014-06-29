#from bottle import route, run, template
from bottle import *
from peewee import *

db = SqliteDatabase('accueil.db')
cssfile = open("style.css","r").read()
css = "<style>"+cssfile+"</style>"
#db = sqlite3.connect('accueil.db')

#db.execute("CREATE TABLE group (id INTEGER PRIMARY KEY, name CHAR(100) NOT NULL, score INTEGER NOT NULL)")

class Group(Model):
    name = CharField()
    score = IntegerField()

    class Meta:
        database = db # this model uses the people database

try:
	Group.create_table()
except OperationalError:
	print("") #Obligatoire sinon bug... WHY?

# Fonctions de créations de comptes
@route('/NewUser')
def newuser():
	html =  '<input id="field"/><button onClick="document.location = \'/NewUser/\'+getElementById(\'field\').value;">Créer</button>'
	return css+html

@route('/NewUser/<name>')
def newuser(name):
	try:
		group = Group.get(Group.name == name)
		return css+"<p style='color : red;'>Erreur, Le groupe "+name+" existe déjà...</p> <script>setTimeout(function() {document.location = '/NewUser';}, 2000);</script>"
	except Group.DoesNotExist:
		group = Group(name=name, score=0)
		group.save()
		#return "New {} score {}".format(group.name, group.score)
		return css+"<p style='color : green'>Le groupe "+name+" à été crée.</p> <script>setTimeout(function() {document.location = '/NewUser';}, 2000);</script>"
	#return template('<b>Hello {{name}}</b>!', name=name)

#Fin des fonctions de créations de comptes

#Acceuil du challenge
@route('/User')
def index():
	html =  'Nom d\'utilisateur : <input id="field"/><button onClick="document.location = \'/User/\'+getElementById(\'field\').value;">Connexion</button>'
	return css+html
@route('/User/<name>')
def index(name):
	try:
		group = Group.get(Group.name == name)

		#group.score += 1
		#group.save()
		return css+"Hello {} score {}".format(group.name, group.score)
	except Group.DoesNotExist:
		#group = Group(name=name, score=0)
		#group.save()
		#return "New {} score {}".format(group.name, group.score)
		return "<script>document.location = '/UtilisateurInconnu'</script>";
	#return template('<b>Hello {{name}}</b>!', name=name)

@route("/UtilisateurInconnu")
def utilisateurInconnu():
	return css+'<p style=\'color : red\'>L\'utilisateur que vous avez entrez n\'existe pas.</p> <script>setTimeout(function() {document.location = \'/User\';}, 2000);</script>'

#@error(404)
#def error404(error):
#    return '<title>Erreur 404</title><H1>Erreur 404 : page inconnue</H1>La page que vous essayez de charger n\'existe pas...'


run(host='localhost', port=8080, debug=True, reloader=True)