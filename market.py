from flask import Flask, render_template
# from markupsafe import escape
app = Flask(__name__)


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
    return render_template('market.html', item_name='Phone')
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

if __name__ == "__main__":
    app.run(debug=True)