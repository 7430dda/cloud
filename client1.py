from flask import Flask, request, render_template_string
from zeep import Client
import os

app = Flask(__name__)

client = Client('https://cloud-00y8.onrender.com/?wsdl')

HTML = '''
    <form method="post">
        Name: <input type="text" name="name">
        <input type="submit" value="Say Hello">
    </form>
    {% if result %}
        <p><b>Result:</b> {{ result }}</p>
    {% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        name = request.form['name']
        result = client.service.say_hello(name)
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
