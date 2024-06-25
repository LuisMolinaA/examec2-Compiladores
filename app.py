from flask import Flask, request, render_template, jsonify
import revisor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    content = request.form['code']
    token_table = []  # List to collect tokens
    result_table = []  # List to collect results
    error_table = []  # List to collect errors
    tokens, error_table, result_table = revisor.check_code(content, token_table, result_table, error_table)
    
    
    response = {
        'tokens': token_table,
        'errors': error_table,
        'syntaxs': result_table,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
