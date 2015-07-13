from google.appengine.api import users 
import webapp2,random,string,urllib

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!</br></br>\n')
        self.response.write('Example\n ')
        self.response.write("<html><body></br><a href='http://natsuko-step2015.appspot.com/convert?message=helloworld'>http://natsuko-step2015.appspot.com/convert?message=helloworld</a></body></html>")
        #self.response.write("<html><body></br><a href='http://natsuko-step2015.appspot.com/convert?message=helloworld'>http://natsuko-step2015.appspot.com/convert?message=helloworld</a></body></html>")

class Second(webapp2.RequestHandler):
	def get(self):
		message=self.request.get('message')
		url="http://step15-krispop.appspot.com/peers"
		l=urllib.urlopen(url)
		line=l.readlines()
		
		for i in line:
			#self.response.write(i+"</br>")
			access=i.strip()+'/convert?message='+message.strip()
			#self.response.write(access+'</br>')
			result=urllib.urlopen(access)
			f=result.read()
			self.response.write(f+'</br>')





class Show(webapp2.RequestHandler):
	def get(self):
		a=self.request.get("message")
		self.response.write(a+'</br>')
		

class Animal(webapp2.RequestHandler):
	def get(self):
		animal=['lemur','weasel','anteater','kangaroo','giraffe','tiger','baboon','leopard','sheep','camel']
		self.response.write(animal[random.randint(0,9)])

class Test(webapp2.RequestHandler):
	def get(self):
		self.response.write('foo was set to %s ?' % self.request.get("foo"))

class Demo(webapp2.RequestHandler):			
	def get(self):
		a=self.request.get("message")
		a=a.lower()
		#a=a.strip()
		#self.response.write(a+'\n')
		b=a[::-1]
		#self.response.write(b+'\n')
		alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ']
		#alphabet=[a-z]
		result=""
		for i in range(len(a)):
			
			num=alphabet.index(b[i])+5
			if num>36: 
				num=num-36
			result+=alphabet[num]
		
		self.response.write('***'+result+'***')

class String(webapp2.RequestHandler):
	def get(self):
		a=self.request.get("message")
		self.response.write(a+"</br>")
		a=a.replace("aiueo","WERTI")
		self.response.write(a+'\n')




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/show', Second),
    ('/animal',Animal),
    ('/print', Test),
    ('/convert', Demo),
    ('/string', String)
], debug=True)
