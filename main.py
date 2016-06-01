import os, os.path
import cherrypy

from app.home import Home
from api.game import Game


if __name__ == '__main__':
    cherrypy.tree.mount(Home())
    cherrypy.tree.mount(Game(), '/game', {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    })
    cherrypy.tree.mount(None, '/static', {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
