from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Country Presentations</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="text-center">Country Presentations</h1>
            <div class="row mt-4">
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body text-center">
                            <h3>🇨🇳 China PDF</h3>
                            <a href="/china" class="btn btn-primary">View Slides</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body text-center">
                            <h3>🇵🇰 Pakistan PDF</h3>
                            <a href="/pakistan" class="btn btn-success">View Slides</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body text-center">
                            <h3>🇰🇪 Kenya PDF</h3>
                            <a href="/kenya" class="btn btn-warning">View Slides</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/china')
def china():
    return "<h1>China Presentation</h1><p>This will show China PDF content</p>"

@app.route('/pakistan')
def pakistan():
    return "<h1>Pakistan Presentation</h1><p>This will show Pakistan PDF content</p>"

@app.route('/kenya')
def kenya():
    return "<h1>Kenya Presentation</h1><p>This will show Kenya PDF content</p>"

if __name__ == '__main__':
    app.run(debug=True)
