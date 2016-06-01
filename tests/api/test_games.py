import cherrypy
import json

from cherrypy.test import helper
from api.game import Game


class TestGamesAPI(helper.CPWebCase):
    def setup_server():
        cherrypy.tree.mount(Game(), '/game', {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
            }
        })

    setup_server = staticmethod(setup_server)

    def test_game_should_return_formatted(self):
        self.getPage("/game/?name=Uncharted")
        self.assertStatus('200 OK')
        self.assertHeader('Content-type', 'application/json')
        self.assertBody(json.dumps({ "game": "Uncharted" }))

    def test_game_and_platform_should_return_formatted(self):
        self.getPage("/game/platform/?name=Uncharted&platform=PS4")
        self.assertStatus('200 OK')
        self.assertHeader('Content-type', 'application/json')
        self.assertBody(json.dumps({ "game": "Uncharted", "platform": "PS4" }))
