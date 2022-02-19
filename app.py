from flask import Flask, render_template, request
from search_bar import SeachBar
from flask_behind_proxy import FlaskBehindProxy
from APIs.four_square_api import search_api

app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = ''

# The app route below is the default home page
@app.route("/", methods=['GET', 'POST'])
def home():
    return(render_template('index.html'))

# The app route below is specifically to test the results.html page. 
# data pulled from the api is dynamically rendured on the webpage
@app.route("/results", methods=['GET', 'POST'])
def results():
    form = SeachBar()
    if form.validate_on_submit():     
        zip = request.form['zip_bar']
        data = request.form['search_bar']
        results_df = search_api(zip,data)
        return(render_template('results.html', results=results_df, form=form))
    return(render_template('results.html', results='' ,form=form, ))

# The app route below is specifically to test the map.html page which is an extension of the results page.
@app.route("/maps", methods=['GET', 'POST'])
def maps():
    form = SeachBar()
    return(render_template('map.html', address='',form=form))


if __name__ == '__main__':
      app.run(debug=True, host="0.0.0.0",port=int(os.environ.get("PORT",8080)))
            