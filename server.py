"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
    'dirty', 'smelly', 'out-of-luck', 'lame', 'sad excuse for a human being', 
    'awful', 'terrible', 'absolutely gut-wrenching', 'smelly like a bad fart']

@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
      <html>
        <head>
          <title>Homepage</title>
        </head>
        <body>
          <center><h1>Hi! This is the home page.</h1>
          <h2><a href='http://localhost:5000/hello'>Click Me!</a></h2>
          </center>
        </body>
      </html>
      """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body><center>
        <h1>Hi There!</h1>
        <form action="/greet">
         <p> What's your name? <input type="text" name="person"></p>
          <p>Choose your compliment below!
          <select name="compliment">
          <option value="awesome">Awesome</option>
          <option value="terrific">Terrific</option>
          <option value="fantastic">Fantastic</option>
          <option value="neato">Neato</option>
          <option value="fantabulous">Fantabulous</option>
          <option value="wowza">Wowza</option>
          <option value="oh-so-not-meh">Oh So Not Meh</option>
          <option value="brilliant">Brilliant</option>
          <option value="ducky">Ducky</option>
          <option value="coolio">Coolio</option>
          <option value="incredible">Incredible</option>
          <option value="wonderful">Wonderful</option>
          <option value="smashing">Smashing</option>
          <option value="lovely">Lovely</option></p>
          <input type="submit" value="Submit">
        </form>
      </center></body>
    </html>
    """

@app.route("/diss")
def diss_person():
  insult = choice(INSULTS) 

  return """
<!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
       JUST KIDDING, YOU ARE {}!!!
      </body>
    </html>
    """.format(insult)

@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
        <br>
        <a href='http://localhost:5000/diss'>Click Me for more compliments!</a>
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
