from google.appengine.api import users 
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class Say(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
			self.response.write('hello, '+ user_nickname())
		else:
			self.redirect(users.create_login_url(self.request.uri))
		self.response.write('guest')
		self.response.write("Say! Hello world!")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/say', Say)
], debug=True)
