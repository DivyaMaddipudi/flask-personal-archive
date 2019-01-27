from flask import Flask, render_template
import os
import sys
from flask import request
import random
import string
from random import randint

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tech-key-search', methods=['POST'])
def result():

    name1 = request.form.get('name1')

    grid = word_search()


    user = {
        'name1': name1,
        'grid': grid
    }

    # return content
    return render_template('result.html', user=user)

def word_search():
    handle = open(r'E:\Tech key search\tech key search.txt')
    words = handle.readlines()
    handle.close()

    words = [random.choice(words).upper().replace(" ' ",'').strip() \
             for _ in range(6)]

    grid_size = 20

    grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

    def print_grid():
        for x in range(grid_size):
            return '\t'*5 + ' ' .join(grid[x])
            return words

    orientations =  [ 'leftright', 'updown', 'diagonalup', 'diagonaldown']

    for word in words:
        word_length = len(word)

        placed = False
        while not placed:

            orientation =  random.choice(orientations)

            if orientation == 'leftright':
                step_x = 1
                step_y = 0
            if orientation == 'updown':
                step_x = 0
                step_y = 1
            if orientation == 'diagonalup':
                step_x = 1
                step_y = 1
            if orientation == 'diagonaldown':
                step_x = 1
                step_y = -1
            x_position = random.randint(0, grid_size)
            y_position = random.randint(0, grid_size)

            ending_x = x_position + word_length*step_x
            ending_y = y_position + word_length * step_y


            if ending_x < 0 or ending_x >= grid_size: continue
            if ending_y < 0 or ending_y >= grid_size: continue

            failed = False

            for i in range(word_length):
                character = word[i]

                new_position_x = x_position + i*step_x
                new_position_y = y_position + i*step_y

                character_at_new_position = grid[new_position_x][new_position_y]
                if character_at_new_position != '_':
                    if character_at_new_position == character:
                        continue
                    else:
                        failed =True
                        break
                if failed:
                    continue
                else:
                    for i in range(word_length):
                        character = word[i]

                        new_position_x = x_position + i * step_x
                        new_position_y = y_position + i * step_y

                        grid[new_position_x][new_position_y] = character

                        placed = True
    for x in range(grid_size):
        for y in range(grid_size):
            if(grid[x][y] == '_'):
                grid[x][y] = random.choice(string.ascii_uppercase)


    print_grid()



if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))

    app.run(host=host, port=5001, use_reloader=False)

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