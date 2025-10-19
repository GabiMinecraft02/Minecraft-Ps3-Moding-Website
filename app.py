from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/robots.txt")
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
