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
        },
        'dynasties': [
            {'name': 'Xia Dynasty', 'period': 'ca. 2100-1600 BCE'},
            {'name': 'Shang Dynasty', 'period': 'ca. 1600-1050 BCE'},
            {'name': 'Zhou Dynasty', 'period': '1046-256 BCE'},
            {'name': 'Qin Dynasty', 'period': '221-206 BCE'},
            {'name': 'Han Dynasty', 'period': '206 BCE-220 CE'},
            {'name': 'Sui Dynasty', 'period': '581-618 CE'},
            {'name': 'Tang Dynasty', 'period': '618-906 CE'},
            {'name': 'Song Dynasty', 'period': '960-1279 CE'},
            {'name': 'Yuan Dynasty', 'period': '1279-1368 CE'},
            {'name': 'Ming Dynasty', 'period': '1368-1644 CE'},
            {'name': 'Qing Dynasty', 'period': '1644-1912 CE'},
            {'name': 'Republic', 'period': '1912-1949 CE'},
            {'name': 'People\'s Republic', 'period': '1949-present'}
        ],
        'historical_spots': [
            {
                'name': 'The Forbidden City',
                'description': 'Imperial Palace located in the heart of Beijing'
            },
            {
                'name': 'The Great Wall',
                'description': 'Defensive structures along northern borders'
            },
            {
                'name': 'The Summer Palace',
                'description': 'Imperial garden with lakes, gardens, and palaces'
            }
        ],
        'natural_spots': [
            {
                'name': 'Zhangjiajie National Park',
                'description': 'Known for beautiful rock formations'
            },
            {
                'name': 'Yangtze River',
                'description': 'China\'s longest and most important river'
            },
            {
                'name': 'West Lake',
                'description': 'Inspires poets and painters throughout history'
            }
        ],
        'cuisine': [
            {
                'name': 'Peking Roasted Duck',
                'description': 'Well-known dish from Beijing, considered a national meal'
            },
            {
                'name': 'Chinese Hot Pot',
                'description': 'Interactive meal with simmering pot of soup'
            },
            {
                'name': 'Dim Sum',
                'description': 'Small plates of dumplings served with tea'
            }
        ]
    }
    return render_template('china.html', data=china_data)

@app.route('/pakistan')
def pakistan():
    pakistan_data = {
        'geography': {
            'location': 'South Asia',
            'borders': 'India, China, Afghanistan, Iran',
            'features': 'Mountains, deserts, fertile plains, rivers',
            'capital': 'Islamabad',
            'largest_city': 'Karachi',
            'population': '240 million (5th most populous)'
        },
        'history': {
            'founded': '1947',
            'civilization': 'Indus Valley Civilization (2600 BC)',
            'influences': 'Mughal, Persian, British'
        },
        'economy': {
            'sectors': 'Agriculture, textiles, industry',
            'produces': 'Wheat, rice, cotton',
            'resources': 'Minerals, coal, natural gas',
            'project': 'China-Pakistan Economic Corridor (CPEC)'
        },
        'tourism': [
            'Hunza, Skardu, and Fairy Meadows in northern regions',
            'Badshahi Mosque in Lahore',
            'Mohenjo-Daro and Taxila',
            'Karakoram Highway'
        ],
        'wildlife': [
            'Snow leopards',
            'Markhor (wild goats)',
            'Bengal tigers',
            'Indus river dolphins'
        ],
        'festivals': [
            'Eid-ul-Fitr and Eid-ul-Adha',
            'Basant (Dragon Festival) in Punjab',
            'Shandur Polo Festival',
            'Pakistan Day (March 23)',
            'Independence Day (August 14)'
        ],
        'cuisine': [
            'Biryani',
            'Nihari',
            'Chapli Kebabs',
            'Saag'
        ],
        'curiosities': [
            'Home to K2, second highest mountain in the world',
            'Indus Valley Civilization location',
            'Largest canal irrigation system in the world',
            'Islamabad considered one of most beautiful capitals',
            'Cricket most popular, field hockey national sport'
        ]
    }
    return render_template('pakistan.html', data=pakistan_data)

@app.route('/kenya')
def kenya():
    kenya_data = {
        'big_five': [
            'Lion', 'Leopard', 'Rhino', 'Elephant', 'Buffalo'
        ],
        'other_animals': [
            'Giraffes', 'Zebras', 'Cheetahs', 'Hippos'
        ],
        'attractions': {
            'migration': 'Great Migration in Maasai Mara',
            'mount_kenya': {
                'height': 'Second-highest in Africa',
                'type': 'Ancient extinct volcano',
                'status': 'UNESCO World Heritage Site',
                'fact': 'Country named after this mountain'
            },
            'mombasa': {
                'description': 'Second-largest city and main port',
                'influences': 'African, Arabic, Portuguese',
                'landmark': 'Fort Jesus (16th-century Portuguese fort)',
                'feature': 'Beautiful white-sand beaches'
            }
        },
        'cuisine': [
            {
                'name': 'Nyama Choma',
                'description': 'National dish - grilled meat (goat or beef)'
            },
            {
                'name': 'Ugali',
                'description': 'Staple food made from maize flour'
            },
            {
                'name': 'Sukuma Wiki',
                'description': 'Collard greens, common side dish'
            },
            {
                'name': 'Chapati',
                'description': 'Flatbread influenced by Indian cuisine'
            }
        ]
    }
    return render_template('kenya.html', data=kenya_data)

if __name__ == '__main__':
    app.run(debug=True)

