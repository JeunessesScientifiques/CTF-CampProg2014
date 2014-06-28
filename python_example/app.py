from bottle import route, run, template


from peewee import *

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    score = IntegerField()

    class Meta:
        database = db # this model uses the people database


@route('/hello/<name>')
def index(name):
    try:
        person = Person.get(Person.name == name)
        person.score += 1
        person.save()
        return "Hello {} score {}".format(person.name, person.score)
    except Person.DoesNotExist:
        person = Person(name=name, score=0)
        person.save()
        return "New {} score {}".format(person.name, person.score)
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080, debug=True)