"""standard freeze script"""

from flask_frozen import Freezer

# instead of "filename," below, use the name of the file that
# runs YOUR Flask app - omit .py from the filename
from videogames import app
from data import detail


app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)



@freezer.register_generator
def num():
    for item in num:
        yield { 'num': item['num'] }

if __name__ == '__main__':
    freezer.freeze()