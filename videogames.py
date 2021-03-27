from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
videogames_list = convert_to_dict("top_20_games.csv")

# create a list of tuples in which the first item is the number
# (Ranking) and the second item is the name (Title of Video Game)
pairs_list = []
for p in videogames_list:
    pairs_list.append( (p['Ranking'], p['Title']) )

# first route (Full List)

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="List of Top 20 Games by Sales Volume")

# second route (Individual Listing)

@app.route('/videogame/<num>')
def detail(num):
    try:
        videogames_dict = videogames_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Video Game Selection: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('videogame.html', videog=videogames_dict, ord=ord, the_title=videogames_dict['Title'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
