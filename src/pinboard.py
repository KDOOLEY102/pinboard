'''
Pinboard : a CSCE 242 project.
Created on May 16, 2012
www.csce242.com

@author: Jose M Vidal <jmvidal@gmail.com>
'''
import webapp2
import jinja2
import os
import logging #for debugging.
from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainPage(webapp2.RequestHandler):
    def get(self):
        templateValues = {}
        if self.request.get('imgUrl') != None:
            templateValues['imgUrl'] = self.request.get('imgUrl')
        if self.request.get('caption') != None:
            templateValues['caption'] = self.request.get('caption')
        templateValues['title'] = 'Pinboard'
        user = users.get_current_user()
        if user:
            templateValues['logout'] = users.create_logout_url('/')
            templateValues['username'] = user.nickname()
        else:
            templateValues['login'] = users.create_login_url('/')
        template = jinja_environment.get_template('main.html')
        self.response.out.write(template.render(templateValues))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
