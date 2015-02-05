import webapp2

from view.urls import endpoints

public_app = webapp2.WSGIApplication(endpoints, debug=True)
