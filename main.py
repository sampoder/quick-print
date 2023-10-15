import os
import logging
import shutil
from flask import Flask, send_from_directory, render_template
from pyngrok import ngrok
from dotenv import load_dotenv
import random
import atexit
import flask.cli
import threading
import subprocess

from words import word_list
from pyfiglet import Figlet
from s1db import S1

load_dotenv()
api = S1(os.getenv('S1_TOKEN'))

app = Flask(__name__)
file_directory = "print"

# Disable unnecessary logging
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True
flask.cli.show_server_banner = lambda *args: None

def create_directory():
		if not os.path.exists(file_directory):
				os.makedirs(file_directory)

def delete_directory():
		os.system('cls' if os.name == 'nt' else 'clear')
		if os.path.exists(file_directory):
				shutil.rmtree(file_directory)

@app.route('/<path:filename>')
def serve_file(filename):
		return send_from_directory(file_directory, filename)

@app.route('/')
def serve_index():
		if os.path.exists(file_directory):
				files = os.listdir(file_directory)
				return render_template("index.html", files=files)
		else:
				return "Directory not found."

def open_directory_in_file_viewer(directory_path):
		if os.name == 'posix':
				subprocess.run(['open', directory_path])
		elif os.name == 'nt':
				subprocess.run(['explorer', directory_path])
		elif os.name == 'mac':
				subprocess.run(['open', directory_path])


if __name__ == '__main__':
		create_directory()
		atexit.register(delete_directory)
		tunnel = ngrok.connect("9472")
		os.system('cls' if os.name == 'nt' else 'clear')
		f = Figlet(font='slant')
		print(f.renderText('Quick Print'))
		word = random.choice(word_list).lower()
		print(f'Visit https://{word}.print.sampoder.com for your files. \n')
		open_directory_in_file_viewer(file_directory)
		api.set(word, tunnel.public_url)
		app.run(host='0.0.0.0', port=9472)
