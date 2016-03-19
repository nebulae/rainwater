import webapp2
import urllib2
import json
import logging
import handlers


class MainHandler(handlers.BaseTemplateHandler):
    def get(self):
        self.render_template("main.html", {})

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
