from flask import Flask, render_template

app = Flask(__name__)

# EXACT PDF CONTENT - Maintaining original structure
pdf_content = {
    'china': {
        'title': 'CHINA',
        'presenter': 'Asiru 阿斯如',
        'slides': [
            {'type': 'cover', 'title': 'CHINA', 'content': ''},
            {'type': 'agenda', 'title': 'AGENDA', 'content': [
                'Basic facts about China',
                'The historical timeline of Chinese dynasties', 
                'China\'s scenic spots',
                'Must-try cuisine'
            ]},
            {'type': 'presenter', 'title': 'PRESENTER', 'content': 'Asiru 阿斯如'},
            {'type': 'greeting', 'title': '大家好 (Dà jiā hǎo)', 'content': 'Hello, everyone'},
            {'type': 'basic_facts', 'title': 'BASIC FACTS', 'content': [
                'China spans approximately 5,250 km from east to west and 5,500 km from north to south.',
                'Land border: 20,000 km long | Shoreline: 14,000 km long.',
                'Biggest population of any country in the world.',
                'Largest country in Asia.',
                'World\'s biggest temperature difference between northern and southern borders.',
                'Over 4,000 years of recorded history.'
            ]},
            {'type': 'dynasties', 'title': 'THE DYNASTIES', 'content': [
                'Xia Dynasty (ca. 2100-1600 BCE)',
                'Shang Dynasty (ca. 1600-1050 BCE)', 
                'Zhou Dynasty (1046-256 BCE)',
                'Qin Dynasty (221-206 BCE)',
                'Han Dynasty (206 BCE-220 CE)',
                'Sui Dynasty (581-618 CE)',
                'Tang Dynasty (618-906 CE)',
                'Song Dynasty (960-1279 CE)',
                'Yuan Dynasty (1279-1368 CE)',
                'Ming Dynasty (1368-1644 CE)',
                'Qing Dynasty (1644-1912 CE)',
                'Republic (1912-1949 CE)',
                'People\'s Republic (1949-present)'
            ]},
            {'type': 'historical_spots', 'title': 'HISTORICAL SCENIC SPOTS', 'content': [
                'THE FORBIDDEN CITY: Imperial Palace in heart of Beijing, must-see for travelers.',
                'THE GREAT WALL: Defensive structures along northern borders.',
                'THE SUMMER PALACE: Lakes, gardens, palaces - imperial garden during Qing dynasty.'
            ]},
            {'type': 'natural_spots', 'title': 'NATURAL SCENIC SPOTS', 'content': [
                'ZHANGJIAJIE NATIONAL PARK: Beautiful rock formations in Wulingyuan Scenic Area.',
                'YANGTZE RIVER: China\'s longest and most important river, world\'s third longest.',
                'WEST LAKE: Beauty inspired poets, painters throughout Chinese history.'
            ]},
            {'type': 'cuisine', 'title': 'MUST-TRY DISHES', 'content': [
                'PEKING ROASTED DUCK: Well-known Beijing dish, considered national meal.',
                'CHINESE HOT POT: Interactive meal with simmering pot of soup.',
                'DIM SUM: Small plates of dumplings served with tea.'
            ]},
            {'type': 'closing', 'title': '谢谢你 (Xiè xiè nín)', 'content': 'Thank you'}
        ]
    },
    'pakistan': {
        'title': 'PAKISTAN',
        'presenter': 'MUHAMMAD USMAN',
        'slides': [
            {'type': 'cover', 'title': 'PAKISTAN', 'content': 'COUNTRY INTRODUCTION'},
            {'type': 'intro', 'title': 'COUNTRY INTRODUCTION', 'content': 'South Asian country known for diverse landscapes, rich history, vibrant culture. Iconic landmarks: Badshahi Mosque, K2, Mohenjo-Daro.'},
            {'type': 'geography', 'title': 'GEOGRAPHY OF PAKISTAN', 'content': [
                'Location: South Asia, borders India, China, Afghanistan, Iran.',
                'Coastline along Arabian Sea.',
                'Features: Mountains, deserts, fertile plains, rivers.',
                'Himalayas & Karakoram contain world\'s highest peaks including K2.',
                'Capital: Islamabad | Largest city: Karachi',
                'Population: 240 million (5th most populous)'
            ]},
            {'type': 'history', 'title': 'HISTORY OF PAKISTAN', 'content': [
                'Founded: 1947 after independence from British rule.',
                'Homeland for Muslims in Indian subcontinent.',
                'Historical heritage: Indus Valley Civilization (2600 BC).',
                'Influences: Mughal, Persian, British rule.'
            ]},
            {'type': 'economy', 'title': 'THE ECONOMY OF PAKISTAN', 'content': [
                'Based on: Agriculture, textiles, industry.',
                'Major producer: Wheat, rice, cotton.',
                'Rich in: Minerals, coal, natural gas.',
                'China-Pakistan Economic Corridor (CPEC) major infrastructure project.',
                'Financial capital: Karachi - major banking center.'
            ]},
            {'type': 'tourism', 'title': 'TOURISM IN PAKISTAN', 'content': [
                'Northern regions: Hunza, Skardu, Fairy Meadows attract trekkers.',
                'Cultural sites: Badshahi Mosque, Mohenjo-Daro, Taxila.',
                'Karakoram Highway: One of highest paved roads, connects to China.'
            ]},
            {'type': 'wildlife', 'title': 'NATURAL LIFE IN PAKISTAN', 'content': [
                'Snow leopards, markhor (wild goats), Bengal tigers, Indus river dolphins.',
                'National parks: Deosai Plains, Hingol, Margalla Hills.',
                'Arabian Sea: Dolphins, turtles.'
            ]},
            {'type': 'festivals', 'title': 'FESTIVALS AND TRADITIONS', 'content': [
                'Eid-ul-Fitr and Eid-ul-Adha (Islamic festivals).',
                'Basant (Dragon Festival) in Punjab - marks spring arrival.',
                'Shandur Polo Festival - world\'s highest polo ground.',
                'Pakistan Day (March 23), Independence Day (August 14).'
            ]},
            {'type': 'cuisine', 'title': 'PAKISTANI CULTURE AND CUISINE', 'content': [
                'Influences: South Asian, Persian, Central Asian.',
                'Language: Urdu unites regions.',
                'Dishes: Biryani, nihari, chapli kebabs, saag.',
                'Tea (chai) staple beverage, mangoes world-famous.'
            ]},
            {'type': 'curiosities', 'title': 'CURIOSITIES ABOUT PAKISTAN', 'content': [
                'Home to K2 - second highest mountain in world.',
                'Indus Valley Civilization location.',
                'Largest canal irrigation system in world.',
                'Islamabad - one of most beautiful capitals.',
                'Cricket most popular, field hockey national sport.'
            ]},
            {'type': 'closing', 'title': 'THANK YOU', 'content': ''}
        ]
    },
    'kenya': {
        'title': 'EXPLORING KENYA',
        'presenter': 'EPHRAIM WAMAE',
        'slides': [
            {'type': 'cover', 'title': 'THE WONDERS OF AFRICA', 'subtitle': 'EXPLORING KENYA'},
            {'type': 'intro', 'title': 'KENYA', 'content': 'A LAND OF SPLENDID DIVERSITY. A JOURNEY THROUGH NATURE, CULTURE, AND CITIES.'},
            {'type': 'wildlife', 'title': 'BIG FIVE', 'content': [
                'Home to "Big Five": Lion, Leopard, Rhino, Elephant, Buffalo.',
                'Great Migration in Maasai Mara - "Seven New Wonders of the World".',
                'Other animals: Giraffes, Zebras, Cheetahs, Hippos.'
            ]},
            {'type': 'attractions', 'title': 'MOUNT KENYA', 'content': [
                'Highest mountain in Kenya, second-highest in Africa.',
                'Ancient extinct volcano.',
                'UNESCO World Heritage Site.',
                'Country named after this mountain!',
                'National pride and challenging peak for climbers.'
            ]},
            {'type': 'cities', 'title': 'MOMBASA - COASTAL CITY', 'content': [
                'Kenya\'s second-largest city and main port.',
                'Blend of African, Arabic, Portuguese influences.',
                'Key landmark: Fort Jesus (16th-century Portuguese fort).',
                'Famous for beautiful white-sand beaches.',
                'Rich, layered history visible in architecture and culture.'
            ]},
            {'type': 'cuisine', 'title': 'THE FLAVORFUL FOOD', 'content': [
                'NYAMA CHOMA: National dish - grilled meat (goat or beef).',
                'UGALI: Staple food from maize flour, eaten with stews.',
                'SUKUMA WIKI: Collard greens, common side dish.',
                'CHAPATI: Flatbread influenced by Indian cuisine.',
                'Hearty and flavorful cuisine.'
            ]},
            {'type': 'closing', 'title': 'ASANTE SANA', 'content': [
                'Thank You Very Much in Swahili.',
                'Unforgettable experience: safari adventures, cultural richness, stunning beaches.',
                'Country of breathtaking contrasts - from lion roars to ocean waves.',
                'Karibu (Welcome)!'
            ]}
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', countries=pdf_content)

@app.route('/presentation/<country_name>')
def show_presentation(country_name):
    if country_name in pdf_content:
        return render_template('pdf_presentation.html', 
                             country=country_name, 
                             data=pdf_content[country_name])
    return "Presentation not found"

if __name__ == '__main__':
    app.run(debug=True)

