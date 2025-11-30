from flask import Flask, render_template

app = Flask(__name__)

# Complete presentation data from your PDFs
countries_data = {
    'china': {
        'title': 'CHINA',
        'flag': '🇨🇳',
        'slides': [
            {'type': 'title', 'title': 'CHINA', 'subtitle': 'Ancient Civilization, Modern Wonder'},
            {'type': 'facts', 'title': 'Basic Facts', 'content': [
                'Size: 5,250 km east-west × 5,500 km north-south',
                'Border: 20,000 km land, 14,000 km shoreline', 
                'Population: Largest in the world',
                'History: Over 4,000 years of recorded history'
            ]},
            {'type': 'history', 'title': 'Chinese Dynasties', 'content': [
                'Xia Dynasty (2100-1600 BCE)',
                'Shang Dynasty (1600-1050 BCE)',
                'Zhou Dynasty (1046-256 BCE)',
                'Qin Dynasty (221-206 BCE)',
                'Han Dynasty (206 BCE-220 CE)'
            ]},
            {'type': 'attractions', 'title': 'Must-Visit Places', 'content': [
                'The Forbidden City - Imperial Palace in Beijing',
                'The Great Wall - Defensive structures',
                'The Summer Palace - Imperial gardens',
                'Zhangjiajie National Park - Beautiful rock formations'
            ]},
            {'type': 'cuisine', 'title': 'Must-Try Dishes', 'content': [
                'Peking Roasted Duck - National dish',
                'Chinese Hot Pot - Interactive meal',
                'Dim Sum - Small plates with tea'
            ]}
        ]
    },
    'pakistan': {
        'title': 'PAKISTAN', 
        'flag': '🇵🇰',
        'slides': [
            {'type': 'title', 'title': 'PAKISTAN', 'subtitle': 'Land of Diverse Landscapes'},
            {'type': 'facts', 'title': 'Geography', 'content': [
                'Location: South Asia',
                'Borders: India, China, Afghanistan, Iran',
                'Capital: Islamabad',
                'Population: 240 million (5th largest)'
            ]},
            {'type': 'history', 'title': 'History & Culture', 'content': [
                'Founded: 1947 after British rule',
                'Ancient: Indus Valley Civilization (2600 BC)',
                'Influences: Mughal, Persian, British',
                'Language: Urdu unites different regions'
            ]},
            {'type': 'attractions', 'title': 'Tourism Highlights', 'content': [
                'Northern Regions: Hunza, Skardu, Fairy Meadows',
                'Badshahi Mosque in Lahore',
                'Mohenjo-Daro ancient city',
                'Karakoram Highway - world\'s highest paved road'
            ]},
            {'type': 'cuisine', 'title': 'Pakistani Cuisine', 'content': [
                'Biryani - Flavorful rice dish',
                'Nihari - Spicy slow-cooked stew',
                'Chapli Kebabs - Minced meat patties',
                'Saag - Leafy greens dish'
            ]}
        ]
    },
    'kenya': {
        'title': 'KENYA',
        'flag': '🇰🇪', 
        'slides': [
            {'type': 'title', 'title': 'KENYA', 'subtitle': 'The Wonders of Africa'},
            {'type': 'facts', 'title': 'Wildlife & Nature', 'content': [
                'Big Five: Lion, Leopard, Rhino, Elephant, Buffalo',
                'Great Migration in Maasai Mara',
                'Mount Kenya - 2nd highest in Africa',
                'Diverse landscapes from savanna to beaches'
            ]},
            {'type': 'attractions', 'title': 'Key Attractions', 'content': [
                'Maasai Mara National Reserve',
                'Mount Kenya - UNESCO World Heritage Site', 
                'Mombasa - Coastal city with Fort Jesus',
                'Beautiful white-sand beaches'
            ]},
            {'type': 'culture', 'title': 'Culture & Cuisine', 'content': [
                'Nyama Choma - Grilled meat national dish',
                'Ugali - Staple maize flour porridge',
                'Sukuma Wiki - Collard greens side dish',
                'Rich tribal heritage and traditions'
            ]},
            {'type': 'highlights', 'title': 'Unique Features', 'content': [
                'Great Migration - One of "Seven New Wonders"',
                'Country named after Mount Kenya',
                'Blend of African, Arabic, Portuguese influences',
                'Friendly people and vibrant culture'
            ]}
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', countries=countries_data)

@app.route('/presentation/<country>')
def presentation(country):
    if country in countries_data:
        return render_template('presentation.html', 
                             country=country, 
                             data=countries_data[country])
    return "Presentation not found"

if __name__ == '__main__':
    app.run(debug=True)
