# Content Security Policy w/ Response Headers

This is a demo of implementing a Flask web server which has a content security policy (CSP) in its response header. While the `<meta http-equiv="Content-Security-Policy" content="your policy here">` method of implementing a CSP is quick and easy for a small website, it has the following limitations:

* you can't use the reporting directive `report-uri` to get security reports when your policy is breached
* in a large or complex website it is easier to dynamically generate a CSP and put it in a response header, than it is to inject a `<meta>` into every HTML document or template in the site

## Install and Usage

**NOTE:** ensure you are using Python 3, not Python 2.

1. To use the server in `server.py` run `pip install flask`
2. Run `python server.py`.
3. Open `localhost:8200` in your browser.
4. Open your browser's debugger and check the console for errors.
5. Change lines 8-11 in `server.py` to implement CSP directives.

## Resources for CSPs

The following are two very useful resources for crafting your own CSP:

* a list of directives for CSPs: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>
* the documentation and examples for CSPs: <https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP>
