from flask import Flask, send_from_directory, jsonify, render_template_string
import os

app = Flask(__name__)

PROJECT_FOLDER = os.path.join(os.getcwd(), "calculator_project_v1")
os.makedirs(PROJECT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    """Главная страница со списком файлов"""
    files = os.listdir(PROJECT_FOLDER)
    html = """
    <h1>Файлы проекта calculator_project_v1</h1>
    <ul>
    {% for file in files %}
        <li><a href="/download/{{file}}">{{file}}</a></li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, files=files)

@app.route("/download/<path:filename>")
def download_file(filename):
    """Отдаёт конкретный файл"""
    return send_from_directory(PROJECT_FOLDER, filename, as_attachment=True)

@app.route("/list_files")
def list_files():
    """Возвращает JSON со списком файлов"""
    files = os.listdir(PROJECT_FOLDER)
    return jsonify(files)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))
