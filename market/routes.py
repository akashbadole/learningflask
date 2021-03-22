from market import app
from flask import render_template
from market.models import Item

# @app.route('/hi')
# def hello():
#     return "Hello Akash badole, learn more, get highly paid job"

@app.route('/')
@app.route('/home')
def home():
    # Templates rendring
    return render_template('home.html')

@app.route('/market')
def market_page():
    # items = [
    # {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    # {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    # {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    items = Item.query.all()
    return render_template('market.html', items=items)
# @app.route('/user/<username>')
# def username_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)
