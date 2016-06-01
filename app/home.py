import cherrypy

from jinja2 import Environment, FileSystemLoader
j_env = Environment(loader=FileSystemLoader('client'))


class Home(object):
    @cherrypy.expose
    def index(self):
        template = j_env.get_template('home.html')
        return template.render()
