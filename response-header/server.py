from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route("/")
def hello():
    page = render_template('./index.html')
    response = Response(page)
    response.headers['Content-Security-Policy'] = "default-src 'self'; " + \
        "style-src 'self' 'unsafe-inline' https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css; " + \
        "script-src 'self' 'unsafe-inline' https://code.jquery.com/jquery-3.3.1.slim.min.js https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js; " + \
        "img-src 'none'; " + \
        "report-uri https://clarx.dev/dev/null;" + \
        "frame-src 'none';"
    return response


if __name__ == "__main__":
    app.run(host='localhost', port=8200)
