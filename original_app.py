from flask import Flask, render_template
from helpers import create_connection, get_adapter



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_page_landing():
    db = create_connection("Bray_Database.db")

    brand_dropdown = []

    brand_dropdown_sql = db.execute("SELECT DISTINCT BRAND FROM VALVES ORDER BY BRAND ASC")

    for row in brand_dropdown_sql:
        brand_dropdown.append(row[0])

    size_dropdown_sql = db.execute("SELECT DISTINCT SIZE FROM VALVES ORDER BY SIZE ASC WHERE = ?")

    return render_template('index.html', brand_dropdown=brand_dropdown)


if __name__ == "__main__":
    app.run()
