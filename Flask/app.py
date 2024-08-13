from flask import Flask , render_template

app = Flask(__name__)   # create instance of the Flask Class

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'The about Page'

if __name__ == '__main__':  # run the app
    app.run()
