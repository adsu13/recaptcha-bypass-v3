# src/app.py

import pychrome
from flask import Flask, request, jsonify
app = Flask(__name__)
browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()
tab.start()
tab.call_method("Console.enable")
def navigate_to(url):
    tab.Page.navigate(url=url, _timeout=500)
    tab.Runtime.evaluate(expression="document.title = 'Não feche essa aba!';")
@app.route("/recaptcha/v3", methods=["GET"])
def solve_recaptcha():
    key = request.args.get('key', '')
    action = request.args.get('action', '')
    script = f"""
        var script = document.createElement('script');
        script.src = 'https://www.google.com/recaptcha/api.js?render={key}';
        document.head.appendChild(script);        
        var resultadoGlobal = 'AAA';
        grecaptcha.execute('{key}', {{action: '{action}'}}).then(function(resultadoRecaptcha) {{
            resultadoGlobal = resultadoRecaptcha;
        }});
    """
    tab.Runtime.evaluate(expression=script)
    result = tab.Runtime.evaluate(expression="resultadoGlobal")
    while not result["result"]["value"].startswith("03A"):
        result = tab.Runtime.evaluate(expression="resultadoGlobal")
    return jsonify({"recaptcha_result": result["result"]["value"]})

if __name__ == "__main__":
    navigate_to("https://example.com") 
    app.run(host='0.0.0.0', port=8082, debug=False)
