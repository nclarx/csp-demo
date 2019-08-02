from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route("/")
def hello():
    page = render_template('./index.html')
    response = Response(page)
    response.headers['Content-Security-Policy'] = "default-src 'self'; " + \
            "style-src 'self'; " + \
            "script-src 'self'; " + \
            "img-src 'self; "
    return response

if __name__ == "__main__":
    app.run(host='localhost', port=8200)

