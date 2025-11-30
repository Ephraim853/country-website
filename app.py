from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Country PDF Presentations</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="text-center mb-4">Country PDF Presentations</h1>
            
            <div class="row">
                <!-- China -->
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body text-center">
                            <h3>🇨🇳 China PDF</h3>
                            <p>Basic facts, dynasties, scenic spots, cuisine</p>
                            <a href="/china" class="btn btn-danger">View China PDF</a>
                        </div>
                    </div>
                </div>
                
                <!-- Pakistan -->
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body text-center">
                            <h3>🇵🇰 Pakistan PDF</h3>
                            <p>Geography, history, tourism, culture</p>
                            <a href="/pakistan" class="btn btn-success">View Pakistan PDF</a>
                        </div>
                    </div>
                </div>
                
                <!-- Kenya -->
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body text-center">
                            <h3>🇰🇪 Kenya PDF</h3>
                            <p>Wildlife, Mount Kenya, Mombasa, food</p>
                            <a href="/kenya" class="btn btn-warning">View Kenya PDF</a>
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
    return """
    <div class="container mt-4">
        <a href="/" class="btn btn-secondary">← Back</a>
        <h1 class="text-center">🇨🇳 CHINA PDF CONTENT</h1>
        
        <div class="card mt-4">
            <div class="card-body">
                <h3>BASIC FACTS</h3>
                <p>• Size: 5,250 km × 5,500 km</p>
                <p>• Population: Largest in world</p>
                <p>• History: 4,000+ years</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>DYNASTIES</h3>
                <p>Xia, Shang, Zhou, Qin, Han, Tang, Song, Ming, Qing</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>SCENIC SPOTS</h3>
                <p>• Forbidden City</p>
                <p>• Great Wall</p>
                <p>• Summer Palace</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>CUISINE</h3>
                <p>• Peking Duck</p>
                <p>• Hot Pot</p>
                <p>• Dim Sum</p>
            </div>
        </div>
    </div>
    """

@app.route('/pakistan')
def pakistan():
    return """
    <div class="container mt-4">
        <a href="/" class="btn btn-secondary">← Back</a>
        <h1 class="text-center">🇵🇰 PAKISTAN PDF CONTENT</h1>
        
        <div class="card mt-4">
            <div class="card-body">
                <h3>GEOGRAPHY</h3>
                <p>• Borders: India, China, Afghanistan, Iran</p>
                <p>• Population: 240 million</p>
                <p>• Capital: Islamabad</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>HISTORY</h3>
                <p>• Founded: 1947</p>
                <p>• Indus Valley Civilization</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>TOURISM</h3>
                <p>• Hunza Valley</p>
                <p>• Badshahi Mosque</p>
                <p>• K2 Mountain</p>
            </div>
        </div>
    </div>
    """

@app.route('/kenya')
def kenya():
    return """
    <div class="container mt-4">
        <a href="/" class="btn btn-secondary">← Back</a>
        <h1 class="text-center">🇰🇪 KENYA PDF CONTENT</h1>
        
        <div class="card mt-4">
            <div class="card-body">
                <h3>WILDLIFE - BIG FIVE</h3>
                <p>• Lion, Leopard, Rhino, Elephant, Buffalo</p>
                <p>• Great Migration in Maasai Mara</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>MOUNT KENYA</h3>
                <p>• Second highest in Africa</p>
                <p>• UNESCO World Heritage Site</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>MOMBASA</h3>
                <p>• Coastal city with Fort Jesus</p>
                <p>• Beautiful beaches</p>
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-body">
                <h3>FOOD</h3>
                <p>• Nyama Choma (grilled meat)</p>
                <p>• Ugali</p>
                <p>• Sukuma Wiki</p>
            </div>
        </div>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)

