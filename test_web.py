from flask import Flask, send_file, render_template, request, redirect, url_for
import os
import datetime
import image_engine
import random

UPLOAD_FOLDER = 'F:/Personal Projects/Certificate Generator/user_uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
	return render_template('home.html')

	
@app.route("/view_image")
def view_image():
	t = datetime.datetime.now()

	my_img = image_engine.draw_cert([request.args["template_val"], [ ("Date", str(t.day)+"/"+str(t.month)+"/"+str(t.year)), ("Name", request.args["name_val"]), ("Sig", request.args["sig_val"]), ("Description", request.args["achievement_val"])], ("Logo", request.args["logo_filename_val"])])
	return send_file(my_img, mimetype='image/png')

@app.route("/test_json")
def test_json():
	return {"my_message": str(datetime.datetime.now())}

def allowed_file(filename):
	return '.' in filename and \
    	filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		'''
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		if file.filename == '':
			flash("No selected file")
			return redirect(request.url)
			'''
		file = request.files['file']
		if file and allowed_file(file.filename):
			t = datetime.datetime.now()
			extension = file.filename.rsplit('.', 1)[1].lower()
			filename = str(t.day)+"-"+str(t.month)+"-"+str(t.year)+"--"+str(t.hour)+"-"+str(t.minute)+"-"+str(t.second)+"--"+str(int(random.random()*100))+"."+extension

			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return filename
	return {"STATUS": "ERROR"}