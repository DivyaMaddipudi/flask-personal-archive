from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/friendship-meter', methods=['POST'])
def result():
    
    name1  = request.form.get('name1')

    name2 = request.form.get('name2')
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    
    rate = friendship_meter(name1,name2)

    
    user = {
        'name1' : name1,
        'name2': name2,
        'rate': rate
    }
    
    #return content
    return render_template('result.html', user=user)

def friendship_meter(name1, name2):
    score = 0
    for n in name1:
        for m in name2:
            if (n in "aeiou") and (m in "aeiou") :
                score += 5
                if (n in "friend") and (m in "friend"):
                    score += 10
    return score

    '''if score < 50:
        print("normal friends")
    elif (score >= 50 and score <= 100):
        print("Friends")
    else:
        print("best friends")'''

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = 5001, use_reloader = False)
    
    
'''
Sources:
    http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
    
    https://www.learnpython.org/en/String_Formatting
    
    https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    
    https://github.com/googlemaps/google-maps-services-python
    
    AIzaSyCRhRz_mw_5wIGgF-I6PUy3js6dcY6zQ6Q
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''