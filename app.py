from flask import (
    Flask,
    jsonify,
    render_template
)
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('data.html')

@app.route('/data')
def data():
    return jsonify({
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'value': random.randint(0, 20)
    })
    # assign color density on a geo map 