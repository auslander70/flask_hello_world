from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
  
@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname, lastname):
    myjediname = jediname(firstname, lastname).JediNameConstructor()
    htmlout = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Your jedi name is {}.
        </p>
    """
    return htmlout.format(firstname, myjediname)


class jediname(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def JediNameConstructor(self):
        part1 = self.firstname[:2]
        part2 = self.lastname[:3]
        name = part2 + part1
        return name

    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))