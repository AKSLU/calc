from flask import Flask, send_from_directory, render_template
import os

MAIN_DIR = os.path.join(os.getcwd(), "calculator_project_v1")

app = Flask(__name__)

@app.route('/install')
def install_page():
    return render_template("install.html")

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(MAIN_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

