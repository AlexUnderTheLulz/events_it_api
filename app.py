from bs4 import BeautifulSoup
from flask import Flask, jsonify
import requests 
import json

app = Flask(__name__)


def get_events():

    url = 'https://it-event-hub.ru/'
    data = []

    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, "html.parser")

    events = soup.find_all('a', class_= 'styles_event__5_HcP')

    for event in events:
        link = "https://it-event-hub.ru" + event.get('href')
        eventName = event.find('h4', class_='styles_event-title__BXZ2b').text
        eventDatetime = event.find('time').text
        eventTags = event.find_all('div', class_='styles_chip__XPG78 styles_chip-primary__jIHo3 styles_chip-small__pw_dS')
        results = [tag.get_text() for tag in eventTags]

        data.append({
            'link': link, 
            'eventName': eventName, 
            'eventDatetime': eventDatetime, 
            'eventsTags': results
        })


    return app.response_class(
        response = json.dumps(data, ensire_ascii = False),
        mimetype = 'application/json' 
    )

@app.route('/api/events', methods = ['GET'])
def events_api():
    return get_events() 

if __name__ == '__main__':
    app.run(debug = True)