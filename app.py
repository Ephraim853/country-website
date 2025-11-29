from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/china')
def china():
    china_data = {
        'basic_facts': {
            'size': '5,250 km (east-west) × 5,500 km (north-south)',
            'border': '20,000 km land border, 14,000 km shoreline',
            'population': 'Largest in the world',
            'history': 'Over 4,000 years of recorded history'
        }
    }
    return render_template('china.html', data=china_data)

@app.route('/pakistan')
def pakistan():
    return render_template('pakistan.html')

@app.route('/kenya')
def kenya():
    return render_template('kenya.html')

if __name__ == '__main__':
    app.run(debug=True)