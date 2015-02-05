import webapp2

from .template import render


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(render((__file__, 'base.html')))
