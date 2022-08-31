from flask import Flask, render_template, url_for, request
import math

from scrapers.aptoide_scraper import ScrapeAppPage



def get_app_info(form):

    app_dict = False

    try:
        aptoid_inst = ScrapeAppPage()
        app_dict = aptoid_inst.extract(url=request.form['hr'])
    except:
        pass

    return app_dict



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    app_dict = "False"
    if request.method == 'POST':

        form = request.form

        app_dict = get_app_info(form)
    
    return render_template('index.html', app_dict=app_dict)

if __name__ == "__main__":
    app.run(debug=True)


