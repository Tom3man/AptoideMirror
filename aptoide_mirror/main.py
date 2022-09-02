from flask import Flask, render_template, request

from scrapers.aptoide_scraper import ScrapeAppPage

aptoid_inst = ScrapeAppPage()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    app_dict = "False"
    if request.method == 'POST':

        app_dict = aptoid_inst.extract(url=request.form['hr'])

    return render_template('index.html', app_dict=app_dict)


if __name__ == "__main__":
    app.run(debug=True)
