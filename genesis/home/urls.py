import webapp2

from . import handlers

endpoints = [
    webapp2.Route('/', handler=handlers.MainHandler)
]
