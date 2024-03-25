from flask import Flask, render_template, request, flash, redirect, send_file
from werkzeug.utils import secure_filename
from Processor import Processor
import shutil
import os

app = Flask(__name__)
proc = Processor()


@app.route("/")
def home():
    clean_images()
    return render_template("main.html")


@app.route("/upload_images_handler", methods=["POST"])
def upload_imges():
    proc.list_image.clear()
    if "files" not in request.files:
        flash("Не могу прочитать файл!")
        return redirect(request.url)
    files = request.files.getlist("files")

    for file in files:
        if file.filename == "":
            flash("Нет выбранного файла!")
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(f"static/images/{filename}")
            proc.list_image.append(f"static/images/{filename}")
            flash("success")
    return render_template("main.html", images = proc.list_image)


@app.route("/predict", methods=["POST"])
def prefict():
    clean_predict()
    range_value = request.form["range_input"]
    proc.proc(float(range_value))
    flash("Успех")
    return render_template("main.html")

def clean_predict():
    if os.path.exists("static/predict/"):
        shutil.rmtree("static/predict/")


def clean_images():
    file_list = os.listdir("static/images/")

    for file_name in file_list:
        if file_name == ".gitkeep":
            continue
        file_path = os.path.join("static/images/", file_name)
        os.remove(file_path)


if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True)
