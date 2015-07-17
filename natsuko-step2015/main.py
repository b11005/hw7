#coding:utf-8
from google.appengine.api import users 
import webapp2,random,string,urllib,binascii

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!</br></br>\n')
        self.response.write('Convert\n ')
        self.response.write("<html><body></br><a href='http://natsuko-step2015.appspot.com/convert?message=helloworld'>http://natsuko-step2015.appspot.com/convert?message=helloworld</a></body></html>")
        self.response.write("</br></br>Convert おまけ<html><body></br><a href='http://natsuko-step2015.appspot.com/convert1?message=helloworld'>http://natsuko-step2015.appspot.com/convert1?message=helloworld</a></body></html>")
        self.response.write("</br></br>Show<html><body></br><a href='http://natsuko-step2015.appspot.com/show?message=helloworld'>http://natsuko-step2015.appspot.com/show?message=helloworld</a></body></html>")
        self.response.write("</br></br>Getword<html><body></br><a href='http://natsuko-step2015.appspot.com/getword?message=helloworld'>http://natsuko-step2015.appspot.com/getword?message=helloworld</a></body></html>")

class Show(webapp2.RequestHandler):
	def get(self):
		message=self.request.get('message')
		url="http://step15-krispop.appspot.com/peers"
		l=urllib.urlopen(url)
		line=l.readlines()
		
		for i in line:
			access=i.strip()+'/convert?message='+message.strip()
			self.response.write(access+'--> ')
			result=urllib.urlopen(access)
			f=result.read()
			self.response.write(f+'</br>')
		

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
		#self.response.write(a+'</br>')
		b=a[::-1]
		alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ']
		result=""
		for i in range(len(a)):
			if i not in alphabet:
				result+=a[-i]
			else:
				num=alphabet.index(b[i])+5
				if num>36: 
					num=num-36
					result+=alphabet[num]
		
		self.response.write('1. ***'+result+'***')

		h=binascii.hexlify(a)
		d={'0':'がおー','1':'ぐさっ','2':'ぱりっ','3':'びゅうびゅう','4':'ぱちぱち','5':'にゃー','6':'ぶうぶう','7':'むしゃー','8':'どしん','9':'すとん','a':'びりっ','b':'くるくる','c':'ぐうぐう','d':'すらっ','e':'ぱったん','f':'にこっ'}
		result2=""
		for i in range(len(b)):
			if h[i] in d.keys():
				result2+=d[h[i]]
			else:
				result2+=d[str(random.randint(0,9))]
			
		self.response.write('</br>2. '+result2)

class Demo1(webapp2.RequestHandler):
	def get(self):
		a=self.request.get("message")
		b=binascii.hexlify(a)
		d={'0':'がおー','1':'ぐさっ','2':'ぱりっ','3':'びゅうびゅう','4':'ぱちぱち','5':'にゃー','6':'ぶうぶう','7':'むしゃー','8':'どしん','9':'すとん','a':'びりっ','b':'くるくる','c':'ぐうぐう','d':'すらっ','e':'ぱったん','f':'にこっ'}
		result=""
		for i in range(len(b)):
			if b[i] in d.keys():
				result+=d[b[i]]
			else:
				result+=d[str(random.randint(0,9))]
			
		self.response.write(result)

class Getword(webapp2.RequestHandler):
	def get(self):
		a=self.request.get("pos")
		d={
		'noun':['book','bag','cell phone','plate','flower','house','tree','dictionary','magazine','pool'],
		'verb':['watch','eat','walk','talk','catch','grab','check','call','quit','apologize'],#,'put','run']
		'adverb':['finaly','madly','slowly','often','only','seldom','cheerfully','badly','lazily','exactly'],
		'adjective':['important','basic','old','medical','poor','impossible','typical','huge','global','afraid'],
		'exclamation':["oh",'oops','uh','well','gosh','what','woo','yeah','yay','wow']
		}
		t=["hello",'good-bey','good morning','good evening','every','happy','soon','later','dear','goodness']
		if a in d:
			self.response.write(d[a][random.randint(0,9)])
		else:
			self.response.write(t[random.randint(0,9)])
		
class Madlib(webapp2.RequestHandler):
	def get(self):
		#message=self.request.get('')
		url="http://step15-krispop.appspot.com/peers"
		l=urllib.urlopen(url)
		line=l.readlines()
		for i in line:
			self.response.write(i+'</br>')
			noun=i.strip()+'/getword?noun'
			verb=i.strip()+'/getword?verb'
			adverb=i.strip()+'/getword?adverb'
			adjective=i.strip()+'/getword?adjective'
			exclamation=i.strip()+'/getword?exclamation'
			#self.response.write(access+)#'</br>')
			re_noun=urllib.urlopen(noun)
			
			re_verb=urllib.urlopen(verb)
			re_adverb=urllib.urlopen(adverb)
			re_adjective=urllib.urlopen(adjective)
			re_exclamation=urllib.urlopen(exclamation)
			result1=re_noun.read()
			result2=re_verb.read()
			result3=re_adverb.read() 
			result4=re_adjective.read()
			result5=re_exclamation.read()
			#self.response.write("It was a rare 14° day in Seattle, so I took a dip in Lake Washington. "+
			#	"%\s lapped against the shore, and the sun beat down on my nose. " %self.request.get()+
			#	"As I Boo-paddled further into the lake, something brushed against my Christmas. "+
			#	"'Oh my goodness!' I cried. In a flash, a shark's fin popped up a few feet away. "+
			#	"I chased the shark on the nose and swam toward the shore. Luckily, sharks aren't very happy swimmers. "+
			#	"I wasn't sure I'd make it, but just then, Bigfoot cruised by on a pizza. 'Hop on,' Bigfoot yelled. "+
			#	"I climbed aboard as the shark narrowly missed my iPhone. Who knew there are sharks in Lake Washington?!</br></br>")
			#self.response.write("%s! Maybe I should ask her to %s. </br>" %(result5, result1)+\
			#	"Afterwards we can go to the top of the %s mountain and look at the wonderful sky as we %s in the car. " %(result4, result2)+\
			#	"Maybe some day we can vacation and spend all week %s. </br>" %result3)
			
		self.response.write(0)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/show', Show),
    ('/animal',Animal),
    ('/print', Test),
    ('/convert', Demo),
    ('/convert1', Demo1),
    ('/getword',Getword),
    ('/madlib', Madlib)
], debug=True)
