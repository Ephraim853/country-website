from flask import Flask, render_template

app = Flask(__name__)

# EXACT content from your PDF files
pdf_content = {
    'china': {
        'title': 'CHINA PRESENTATION',
        'slides': [
            {'title': 'CHINA', 'content': 'Basic facts, Historical timeline, Scenic spots, Must-try cuisine'},
            {'title': 'PRESENTER', 'content': 'Asiru 阿斯如'},
            {'title': 'GREETING', 'content': '大家好 - Hello everyone'},
            {'title': 'BASIC FACTS', 'content': '• Size: 5,250 km × 5,500 km\n• Border: 20,000 km land, 14,000 km shoreline\n• Population: Largest in world\n• History: 4,000+ years recorded history'},
            {'title': 'CHINESE DYNASTIES', 'content': 'Xia, Shang, Zhou, Qin, Han, Sui, Tang, Song, Yuan, Ming, Qing'},
            {'title': 'HISTORICAL SPOTS', 'content': '• The Forbidden City\n• The Great Wall\n• The Summer Palace'},
            {'title': 'NATURAL SPOTS', 'content': '• Zhangjiajie National Park\n• Yangtze River\n• West Lake'},
            {'title': 'CHINESE CUISINE', 'content': '• Peking Roasted Duck\n• Chinese Hot Pot\n• Dim Sum'},
            {'title': 'THANK YOU', 'content': '谢谢你 - Thank you'}
        ]
    },
    'pakistan': {
        'title': 'PAKISTAN PRESENTATION',
        'slides': [
            {'title': 'PAKISTAN', 'content': 'South Asian country with diverse landscapes, rich history, vibrant culture'},
            {'title': 'GEOGRAPHY', 'content': '• Borders: India, China, Afghanistan, Iran\n• Mountains, deserts, fertile plains\n• Capital: Islamabad\n• Population: 240 million (5th largest)'},
            {'title': 'HISTORY', 'content': '• Founded: 1947 after British rule\n• Indus Valley Civilization (2600 BC)\n• Mughal, Persian, British influences'},
            {'title': 'ECONOMY', 'content': '• Agriculture, textiles, industry\n• Major producer of wheat, rice, cotton\n• China-Pakistan Economic Corridor (CPEC)'},
            {'title': 'TOURISM', 'content': '• Northern regions: Hunza, Skardu, Fairy Meadows\n• Badshahi Mosque, Mohenjo-Daro\n• Karakoram Highway (world\'s highest paved road)'},
            {'title': 'WILDLIFE', 'content': '• Snow leopards, markhor, Bengal tigers\n• Indus river dolphins\n• National parks: Deosai Plains, Hingol'},
            {'title': 'FESTIVALS', 'content': '• Eid-ul-Fitr, Eid-ul-Adha\n• Basant (Dragon Festival)\n• Shandur Polo Festival'},
            {'title': 'CUISINE', 'content': '• Biryani, nihari, chapli kebabs\n• Saag, chai tea\n• World-famous mangoes'},
            {'title': 'CURIOSITIES', 'content': '• K2 - 2nd highest mountain\n• Largest canal irrigation system\n• Cricket most popular sport'}
        ]
    },
    'kenya': {
        'title': 'KENYA PRESENTATION',
        'slides': [
            {'title': 'THE WONDERS OF AFRICA', 'content': 'EXPLORING KENYA'},
            {'title': 'INTRODUCTION', 'content': 'KENYA, A LAND OF SPLENDID DIVERSITY. A JOURNEY THROUGH NATURE, CULTURE, AND CITIES.'},
            {'title': 'BIG FIVE WILDLIFE', 'content': '• Lion, Leopard, Rhino, Elephant, Buffalo\n• Great Migration in Maasai Mara\n• Giraffes, Zebras, Cheetahs, Hippos'},
            {'title': 'MOUNT KENYA', 'content': '• Highest mountain in Kenya\n• Second-highest in Africa\n• Ancient extinct volcano\n• UNESCO World Heritage Site\n• Country named after this mountain'},
            {'title': 'MOMBASA', 'content': '• Kenya\'s second-largest city\n• Main port city\n• African, Arabic, Portuguese influences\n• Fort Jesus (16th century)\n• Beautiful white-sand beaches'},
            {'title': 'KENYAN CUISINE', 'content': '• Nyama Choma - grilled meat (national dish)\n• Ugali - maize flour porridge\n• Sukuma Wiki - collard greens\n• Chapati - flatbread'},
            {'title': 'CLOSING', 'content': 'Asante Sana - Thank You Very Much\nKenya offers unforgettable safari adventures, cultural richness, and stunning beaches.'}
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', countries=pdf_content)

@app.route('/presentation/<country>')
def show_presentation(country):
    if country in pdf_content:
        return render_template('presentation.html', 
                             country=country, 
                             data=pdf_content[country])
    return "Presentation not found"

if __name__ == '__main__':
    app.run(debug=True)
