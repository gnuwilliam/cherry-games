import cherrypy

@cherrypy.popargs('name')
class Game(object):
    exposed = True

    def __init__(self):
        self.platform = Platform()

    @cherrypy.tools.json_out()
    def GET(self, name):
        return { "game": name }


@cherrypy.popargs('platform')
class Platform(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, name, platform):
        return { "game": name, "platform": platform }
