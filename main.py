from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
from Processor import Processor
import shutil
import os

app = Flask(__name__)
proc = Processor()

image_list = []

@app.route("/")
def home():
  return render_template('main.html')

@app.route("/upload_images_handler", methods = ["POST"])
def upload_imges():
  if 'files' not in request.files:
    flash("Не могу прочитать файл!")
    return redirect(request.url)
  files = request.files.getlist('files')
  
  for file in files:
    if file.filename == "":
      flash("Нет выбранного файла!")
      redirect(request.url)
  
    if file:
      filename = secure_filename(file.filename)
      file.save(f"static/images/{filename}")
      image_list.append(f"static/images/{filename}")
      flash("success")
  return render_template('main.html')

@app.route("/predict", methods=["POST"])
def prefict():
  if os.path.exists("static/predict/"):
    shutil.rmtree("static/predict/")
  range_value = request.form['range_input']
  print(image_list)
  proc.proc(float(range_value), image_list)
  flash("Успех")
  return render_template('main.html')


if __name__ == "__main__":
  app.secret_key = 'super secret key'
  app.run(debug=True)