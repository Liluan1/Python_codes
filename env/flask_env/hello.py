from flask import Flask,render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name = None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return 'index page'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(host='0.0.0.0')
