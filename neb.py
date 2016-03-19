import webapp2
# import urllib2
# import json
# import logging
import handlers

from google.appengine.api import users


class NebsHandler(handlers.AdminAuthenticatedTemplateHandler):
    def get(self):
        self.render_template("admin.html", {'logout': users.create_logout_url(self.request.url)})

app = webapp2.WSGIApplication([
    ('/neb', NebsHandler)
], debug=True)
