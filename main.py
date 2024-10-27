from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'password',
        database = 'Pokemon'
    )
    return connection

@app.route('/', methods = {'GET', 'POST'})
def get_pokemon():

    # when accessing any host, a get request is automatically sent from the browser to the server, that is why get is called automatically
    if request.method == 'GET':
        return render_template('pokemon.html')

    if request.method == 'POST':

        pokemon_id = request.form['pokemon_id']
        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT master_id, species, type1, type2 FROM pokemon_data WHERE master_id = %s", (pokemon_id))

        pokemon = cursor.fetchone() 

        if pokemon:
            return render_template('pokemon.html', pokemon_id = pokemon[0], species = pokemon[1], type1 = pokemon[2], type2 = pokemon[3])

        else:
            return render_template('pokemon.html', error = "Pokemon not found.")


app.run(debug=True, host = '0.0.0.0', port= 80)