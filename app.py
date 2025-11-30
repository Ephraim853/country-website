from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>World Explorer</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="/">🌍 World Explorer</a>
            </div>
        </nav>
        <div class="container mt-4">
            <h1>Welcome to World Explorer! 🎉</h1>
            <p>Your website is FINALLY working!</p>
            <div class="mt-4">
                <a href="/china" class="btn btn-danger">🇨🇳 China</a>
                <a href="/pakistan" class="btn btn-success">🇵🇰 Pakistan</a>
                <a href="/kenya" class="btn btn-warning">🇰🇪 Kenya</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/china')
def china():
    return "<h1>🇨🇳 China</h1><p>China page works! <a href='/'>Home</a></p>"

@app.route('/pakistan')
def pakistan():
    return "<h1>🇵🇰 Pakistan</h1><p>Pakistan page works! <a href='/'>Home</a></p>"

@app.route('/kenya')
def kenya():
    return "<h1>🇰🇪 Kenya</h1><p>Kenya page works! <a href='/'>Home</a></p>"

if __name__ == '__main__':
    app.run(debug=True)