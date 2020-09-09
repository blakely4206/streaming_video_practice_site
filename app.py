import os
from flask import Flask, session, render_template, request, redirect, url_for
import xml.etree.ElementTree as xml

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")

@app.route("/<string:guid>", methods=["GET", "POST"])
def play(guid):    
    tree = xml.parse("./static/metadata.xml")
    root = tree.getroot()
    
#    for x in root.findall('./video'):
 #       for child in x:
 #           if(child.tag == "GUID" and child.text == guid):                
 #               print(child.tag, " ", child.text)

    video = "./static/videos/" + guid + ".mp4"
    poster = "./static/posters/" + guid + ".jpg"

    return render_template("video.html", video=video, poster=poster)