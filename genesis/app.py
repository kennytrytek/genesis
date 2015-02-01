import webapp2

from home.urls import endpoints as home_endpoints

public_endpoints = []
public_endpoints += home_endpoints

public_app = webapp2.WSGIApplication(public_endpoints, debug=True)
