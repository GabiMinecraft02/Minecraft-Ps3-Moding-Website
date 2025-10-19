from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route principale
@app.route("/")
def home():
    return render_template("index.html")

# Route pour robots.txt
@app.route("/robots.txt")
def robots():
    return send_from_directory('.', 'robots.txt')

# Route pour sitemap.xml
@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

# Route pour fichier Google verification
@app.route("/googlea128813747473c36.html")
def google_verification():
    return send_from_directory('.', 'googlea128813747473c36.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
