from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route("/")
def hello():
    page = render_template('./index.html')
    response = Response(page)
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8200)
