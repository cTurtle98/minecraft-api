"""
Minecraft API
By Ciaran Farley ciaran@cturtle98.com

Version 1.0.6

main file
"""

# import stuff
from flask import Flask
from flask import request
import os

#vars
SCREEN_NAME = "minecraft"

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

@app.route('/whitelist/add/', methods=['POST', 'GET'])
def whitelist_add():

	# get the minecraft username from the request
	uname = request.args.get('u')
	
	if (app.config["DEBUG"] == True):
	    print("WHITELIST REQUEST: " + uname)
	
	#send the command to the minecraft server
	os.system("screen -S " + SCREEN_NAME + " -X stuff \'whitelist add " + uname + "\015\'")
	
	#return ok
	return 200

# run flask
app.run(port=8080)
