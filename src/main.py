import cherrypy
import os.path
import mako.template
import mako.lookup
import random
#import page_index
#import page_signup
#import page_posts
#import page_test

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__)])

class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(names.name)
        t = lookup.get_template("page_index.html")
        return t.render(name=n)
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        return page_posts.get()
    @cherrypy.expose
    def test(self):
        return page_test.get()
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
