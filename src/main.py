from jinja2 import Environment, FileSystemLoader
from bottle import route, run
import bottle
import random


JINJA_ENV = Environment(
    loader=FileSystemLoader('templates/'),
    extensions=['jinja2.ext.autoescape']
)

@route('/hi/<name>')
def say_hi(name):
    return respond('hi.html',
    	{
	    'name': name
	})

@route('/image')
def display_image():
    return respond('image.html',
       {
           'red': random.randint(0,255),
		   'green': random.randint(0,255),
		   'blue': random.randint(0,255)
       })
	   
@route('/static/<asset:path>')
def serve_asset(asset):
    return bottle.static_file(asset, root='static/')

def respond(template_file, params):
    tpl = JINJA_ENV.get_template(template_file)
    return tpl.render(**params)

run(host='localhost', port='8080', debug=True)
