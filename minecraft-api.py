"""
Minecraft API
By Ciaran Farley ciaran@cturtle98.com

Version 1.0.3

main file
"""

# import stuff
from flask import Flask
from flask import request
import os

#vars
SCREEN_NAME = minecraft

#setup flask
app = Flask(__name__)

#enable flask debug
app.config["DEBUG"] = True

@app.route('/')
def home():
	return ''' \
	you have reached cturtle98 minecraft api
	see https://github.com/cTurtle98/minecraft-api
	'''

@app.route('/whitelist/add/', methods=['POST'])
def whitelist_add():

	# get the minecraft username from the request
	uname = request.args.get('u')

	os.system("screen -S " + SCREEN_NAME + " -X stuff \'whitelist add " + uname + "\015\'")

# run flask
@app.run(port=8080)
