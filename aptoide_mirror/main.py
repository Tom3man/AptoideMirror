from flask import Flask, render_template, request

from scrapers.aptoide_scraper import ScrapeAppPage

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    app_dict = "False"
    if request.method == 'POST':

        aptoid_inst = ScrapeAppPage(url=request.form['hr'])
        app_dict = aptoid_inst.extracted_dict

    return render_template('index.html', app_dict=app_dict)


if __name__ == "__main__":
    app.run(debug=True)
