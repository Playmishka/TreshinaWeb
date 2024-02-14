from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

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
  return render_template('main.html')


if __name__ == "__main__":
  app.secret_key = 'super secret key'
  app.run(debug=True)