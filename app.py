from flask import Flask, render_template

app = Flask(__name__)

# EXACT data from your PDF slides
presentations = {
    'china': {
        'title': 'CHINA',
        'presenter': 'Asiru 阿斯如',
        'slides': [
            {'type': 'title', 'content': 'CHINA', 'subtitle': ''},
            {'type': 'agenda', 'content': 'Basic facts, Historical timeline, Scenic spots, Must-try cuisine'},
            {'type': 'hello', 'content': '大家好 - Hello everyone'},
            {'type': 'basic_facts', 'content': 'Size: 5,250km × 5,500km, Population: Largest in world, History: 4,000+ years'},
            {'type': 'dynasties', 'content': 'Xia, Shang, Zhou, Qin, Han, Tang, Song, Ming, Qing dynasties'},
            {'type': 'historical_spots', 'content': 'Forbidden City, Great Wall, Summer Palace'},
            {'type': 'natural_spots', 'content': 'Zhangjiajie, Yangtze River, West Lake'},
            {'type': 'cuisine', 'content': 'Peking Duck, Hot Pot, Dim Sum'},
            {'type': 'thank_you', 'content': '谢谢你 - Thank you'}
        ]
    },
    'pakistan': {
        'title': 'PAKISTAN', 
        'presenter': 'MUHAMMAD USMAN',
        'slides': [
            {'type': 'title', 'content': 'PAKISTAN', 'subtitle': 'Diverse landscapes, rich history, vibrant culture'},
            {'type': 'geography', 'content': 'South Asia, borders India/China/Afghanistan/Iran, mountains/deserts/plains'},
            {'type': 'history', 'content': 'Founded 1947, Indus Valley Civilization, Mughal/Persian/British influences'},
            {'type': 'economy', 'content': 'Agriculture, textiles, China-Pakistan Economic Corridor (CPEC)'},
            {'type': 'tourism', 'content': 'Hunza Valley, Badshahi Mosque, Mohenjo-Daro, Karakoram Highway'},
            {'type': 'wildlife', 'content': 'Snow leopards, markhor, Bengal tigers, Indus dolphins'},
            {'type': 'festivals', 'content': 'Eid, Basant, Shandur Polo Festival, Pakistan Day'},
            {'type': 'cuisine', 'content': 'Biryani, nihari, chapli kebabs, saag'},
            {'type': 'curiosities', 'content': 'K2 mountain, ancient civilization, largest irrigation system'}
        ]
    },
    'kenya': {
        'title': 'KENYA',
        'presenter': 'EPHRAIM WAMAE', 
        'slides': [
            {'type': 'title', 'content': 'THE WONDERS OF AFRICA', 'subtitle': 'EXPLORING KENYA'},
            {'type': 'intro', 'content': 'KENYA, A LAND OF SPLENDID DIVERSITY. A JOURNEY THROUGH NATURE, CULTURE, AND CITIES.'},
            {'type': 'big_five', 'content': 'Lion, Leopard, Rhino, Elephant, Buffalo. Great Migration in Maasai Mara.'},
            {'type': 'mount_kenya', 'content': 'Tallest mountain in Kenya, extinct volcano, UNESCO site, country named after it'},
            {'type': 'mombasa', 'content': 'Coastal city, African/Arabic/Portuguese influences, Fort Jesus, white-sand beaches'},
            {'type': 'cuisine', 'content': 'Nyama Choma (grilled meat), Ugali, Sukuma Wiki, Chapati'},
            {'type': 'thank_you', 'content': 'Asante Sana - Thank you very much'}
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', presentations=presentations)

@app.route('/presentation/<country_name>')
def show_presentation(country_name):
    if country_name in presentations:
        return render_template('slides.html', 
                             country=country_name, 
                             data=presentations[country_name])
    return "Presentation not found"

if __name__ == '__main__':
    app.run(debug=True)

