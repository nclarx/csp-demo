# Content Security Policy Demo

This repo contains some examples for implementations of content security policies using a `<meta>` tag, and has a python script that hosts an `index.html` using Flask with a content security policy response header.

* `index.html` -  is a HTML template with Bootstrap scripts and stylesheet.
* `index-sln.html` - has a CSP with some extra directives implemented.
* Run `server.py` to start a server and modify the CSP response header and add your own directives, check `templates` and `static` for the HTML and CSS files (note: you don't need a `<meta>` element with a CSP if you use a CSP repsonse header)
