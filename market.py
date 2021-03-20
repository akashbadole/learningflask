from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Akash badole, learn more, get highly paid job"

@app.route('/hi')
def hi():
    return "Hi, thanks for visiting"

@app.route('/user/<username>')
def username_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(debug=True)