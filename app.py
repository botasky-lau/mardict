#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from views import *
from config import DEBUG
from chat import XmppHandler

application = webapp.WSGIApplication(
    [
        ('/',Index),
        ('/help/',Help),
        ('/user/',User),
        ('/admindict/',AdminDict),
        ('/user/history/',History),
        ('/user/mardict\.xml', XMLExport),
        ('/user/import/', XMLImport),
        ('/god/',God),
        ('/_ah/xmpp/message/chat/', XmppHandler),
        ('.*', Error404),
    ],
    debug=DEBUG,
)

def run():
    run_wsgi_app(application)

if "__main__" == __name__:
    run()
