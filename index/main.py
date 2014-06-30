from bottle import *
from peewee import *
import csv
from parse import *

db = SqliteDatabase('accueil.db')
cssfile_ = open("style.css","r")
cssfile = cssfile_.read()
cssfile_.close()

css = "<style>"+cssfile+"</style>"

class Group(Model):
    name = CharField()
    score = IntegerField()
    mission_ok = CharField()

    class Meta:
        database = db # this model uses the people database

try:
	Group.create_table()
except OperationalError:
	print("") #Obligatoire sinon bug... WHY?


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
		group = Group(name=name, score=0, mission_ok="")
		group.save()
		#return "New {} score {}".format(group.name, group.score)
		return css+"<p style='color : green'>Le groupe "+name+" à été crée.</p> <script>setTimeout(function() {document.location = '/NewUser';}, 2000);</script>"
	#return template('<b>Hello {{name}}</b>!', name=name)

#Fin des fonctions de créations de comptes

#Acceuil du challenge
@route('/User')
def index():
	js = "var name = getElementById(\'field\').value; document.location = \'/User/\'+name;"
	html =  '<div class="box">Equipe : <input id="field"/><button onClick="'+js+'">Connexion</button></div>'
	html+= "<center><h3>Equipes</h3>" 
	for n in Group.select() :
			html+= n.name+"<br/>"
	html+="</center>"
	return css+html

@route('/')
@route('/User/')
def uservide():
	redirect("/User")

@route('/User/<name>')
@view('index.tpl')
def index(name):
	try:
		group = Group.get(Group.name == name)
		groups = Group.select()
		title = "The Challenge"

		return {'cssfile': cssfile,'title':"The challenge","name":group.name,'score':group.score,'groups':groups,"mission_ok":group.mission_ok}
	except Group.DoesNotExist:
		redirect("/UtilisateurInconnu")

@route('/Challenge/<id>', method='post')
def valideSecret(id):
	name =  request.forms.get('name')
	id = request.forms.get('id')
	secret = request.forms.get('secret')
	group = Group.get(Group.name == name)
	
	challenges = []
	with open('challenges.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader :
			if row[0] == id : 
				print("id ok")
				if not row[0] in group.mission_ok:
					print('"'+row[0]+'"')
					print('"'+group.mission_ok+'"')
					if str(secret) == str(row[3]):
						score = int(row[4])
						mission_ok = (str(row[0])+"\n")
						group.mission_ok += mission_ok
						group.score += score
						group.save()
						print("score saved")
	redirect('/User/'+name)


@route("/UtilisateurInconnu")
def utilisateurInconnu():
	return css+'<p style=\'color : red\'>L\'utilisateur que vous avez entrez n\'existe pas.</p> <script>setTimeout(function() {document.location = \'/User\';}, 2000);</script>'

@error(404)
def error404(error):
    return '<title>Erreur 404</title><H1>Erreur 404 : page inconnue</H1>La page que vous essayez de charger n\'existe pas...'


run(host='localhost', port=8080, debug=True, reloader=True)