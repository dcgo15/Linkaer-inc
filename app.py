__author__ = "Daniel Gomes"



from flask import Flask,request, render_template
from pytube import YouTube
import pyshorteners


NOME = "LINKAER"

app = Flask(__name__)


@app.route("/yt", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        link_video = request.form.get("video")
        yt = YouTube(link_video)
        yt.streams.get_highest_resolution().download()
        
        
        
    return render_template("index.html")

@app.route("/link", methods=["GET", "POST"])
def links():
    
    if request.method == "POST":
        link_encurtado = request.form.get("link")
        link = pyshorteners.Shortener().tinyurl.short(link_encurtado)

        return "Seu link é: " + link
        
    
    return render_template("encurtador.html")

if __name__ == "__main__":
    app.run(port="2200",debug=True)
