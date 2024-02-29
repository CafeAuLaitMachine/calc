from flask import Flask, render_template, request
import json
import re
from test import evaluate_postfix, infix_to_postfix

app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.json
    print(data)
    pattern = r'\d+\.\d+|\d+|\+|\-|\*|\/|\^|\(|\)'
    fixed_exp = re.findall(pattern, data)
    if fixed_exp[0] == '-':
        fixed_exp.remove(fixed_exp[0])
        fixed_exp[0] = "-" + fixed_exp[0]
    print(fixed_exp)
    result = evaluate_postfix(infix_to_postfix(fixed_exp))
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)
