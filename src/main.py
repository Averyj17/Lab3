import cherrypy
import os.path
import datetime
import mako.template
import mako.lookup
import random
import names
import pictures


import page_test

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(directories=[os.path.dirname(__file__)])

class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(names.name)
        t = lookup.get_template("index.html")
        return t.render(name=n)
    @cherrypy.expose
    def signup(self):
        t = lookup.get_template("signup.html")
        return t.render()
    @cherrypy.expose
    def posts(self):
        days = []
        hours = []
        minutes = []
        r_list = []
        for i in range(10):
            x = datetime.timedelta(minutes=random.randrange(8000))
            day = x.days
            hoursago = int( x.seconds / 3600 )
            minutesago = round((x.seconds/60) - hoursago*60)

            r_int = random.randint(1,1000000)

            days.append(day)
            hours.append(hoursago)
            minutes.append(minutesago)

            r_list.append(r_int)
        

        t = lookup.get_template("posts.html")
        return t.render(hour=hours, mins=minutes, d = days, v= r_list)
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
