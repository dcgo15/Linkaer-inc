__author__ = "Daniel Gomes"


from flask import Flask,request, render_template
import pyshorteners


NOME = "LINKAER"

app = Flask(__name__)

@app.route("/insta", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        link_video = request.form.get("video")
        return "Seu link é: " + link_video
    return render_template("index.html")

@app.route("/link", methods=["GET", "POST"])
def links():
    if request.method == "POST":
        link_encurtado = request.form.get("link")
        link = pyshorteners.Shortener().tinyurl.short(link_encurtado)
        return "Seu link é: " + link
    return render_template("encurtador.html")

if __name__ == "__main__":
    app.run(port="1100",debug=True)
