import webapp2

from .base import handlers

endpoints = [
    webapp2.Route('/', handler=handlers.MainHandler)
]
