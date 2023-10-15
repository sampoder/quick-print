import os
import logging
import shutil
from flask import Flask, send_from_directory, render_template
import atexit
from pyngrok import ngrok
import flask.cli
flask.cli.show_server_banner = lambda *args: None

app = Flask(__name__)
file_directory = "print"

log = logging.getLogger('werkzeug')
log.disabled = True

app.logger.disabled = True

def create_directory():
		if not os.path.exists(file_directory):
				os.makedirs(file_directory)

def delete_directory():
		if os.path.exists(file_directory):
				shutil.rmtree(file_directory)

@app.route('/<path:filename>')
def serve_file(filename):
		return send_from_directory(file_directory, filename)
		
@app.route('/')
def serve_index():
		if os.path.exists(file_directory):
				files = os.listdir(file_directory)
				print(files)
				return render_template("index.html", files=files)
		else:
				return "Directory not found."
				

if __name__ == '__main__':
		create_directory()
		atexit.register(delete_directory)
		tunnel = ngrok.connect("9472")
		print(tunnel)
		app.run(host='0.0.0.0', port=9472)
		


