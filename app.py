from flask import Flask, render_template, request, jsonify
from helpers import get_adapter, create_connection
from flask_wtf import FlaskForm
from wtforms import SelectField
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Bray_Database.db")

db = create_connection(db_path)

# db = create_connection("Bray_Database.db")


class Form(FlaskForm):
    brand = SelectField('brand', choices=[])
    serie = SelectField('serie', choices=[])
    size = SelectField('size', choices=[])
    act_type = SelectField('act_type', choices=[])
    act_size = SelectField('act_size', choices=[])


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        form = Form()

        form.brand.choices = [row[0] for row in db.execute("SELECT DISTINCT BRAND FROM VALVES ORDER BY BRAND ASC")]
        # form.serie.choices = [row[0] for row in db.execute("SELECT DISTINCT SERIE FROM VALVES WHERE BRAND = 'BRAY' "
        #                                                    "ORDER BY SERIE ASC")]
        # form.size.choices = [row[0] for row in db.execute("SELECT DISTINCT SIZE FROM VALVES WHERE BRAND = 'BRAY' AND "
        #                                                   "SERIE = 'S20' ORDER BY SIZE ASC")]
        form.act_type.choices = [row[0] for row in db.execute("SELECT DISTINCT TYPE FROM ACTUATORS ORDER BY TYPE ASC")]
        # form.act_size.choices = [row[0] for row in db.execute("SELECT DISTINCT SIZE FROM ACTUATORS "
        #                                                       "WHERE TYPE = 'ELECTRIC' ORDER BY SIZE ASC")]



        return render_template('index.html', form=form)

    if request.method == 'POST':

        form = Form()

        form.brand.choices = [row[0] for row in db.execute("SELECT DISTINCT BRAND FROM VALVES ORDER BY BRAND ASC")]
        form.serie.choices = [row[0] for row in db.execute("SELECT DISTINCT SERIE FROM VALVES WHERE BRAND = 'BRAY' "
                                                           "ORDER BY SERIE ASC")]
        form.size.choices = [row[0] for row in db.execute("SELECT DISTINCT SIZE FROM VALVES WHERE BRAND = 'BRAY' AND "
                                                          "SERIE = 'S20' ORDER BY SIZE ASC")]
        form.act_type.choices = [row[0] for row in db.execute("SELECT DISTINCT TYPE FROM ACTUATORS ORDER BY TYPE ASC")]
        form.act_size.choices = [row[0] for row in db.execute("SELECT DISTINCT SIZE FROM ACTUATORS "
                                                              "WHERE TYPE = 'ELECTRIC' ORDER BY SIZE ASC")]

        brand = request.form['brand']
        serie = request.form['serie']
        size = request.form['size']
        act_type = request.form['act_type']
        act_size = request.form['act_size']

        result = get_adapter(brand,serie,size,act_type,act_size)
        print(result)

        return render_template('index.html', form=form, result=result[0], part_number=result[1], brand=brand, serie=serie, size=size,
                               act_type=act_type, act_size=act_size)

@app.route('/serie/<brand>')
def serie(brand):
    series = db.execute("SELECT DISTINCT SERIE FROM VALVES WHERE BRAND = ? ORDER BY SERIE ASC", (brand,))

    serie_array = []

    for serie in series:
        serie_array.append(serie[0])

    return jsonify({'series': serie_array})

@app.route('/size/<serie>/<brand>')
def size(brand, serie):
    sizes = db.execute("SELECT DISTINCT SIZE FROM VALVES WHERE BRAND = ? AND SERIE = ? ORDER BY SIZE ASC", (brand, serie,))

    size_array = []

    for size in sizes:
        size_array.append(f'{size[0]}"')

    return jsonify({'sizes': size_array})

@app.route('/act_size/<act_type>/')
def actSize(act_type):
    act_sizes = db.execute("SELECT DISTINCT SIZE FROM ACTUATORS WHERE TYPE = ? ORDER BY SIZE ASC", (act_type,))

    act_size_array = []

    for act_size in act_sizes:
        act_size_array.append(act_size[0])

    return jsonify({'act_sizes': act_size_array})


if __name__ == '__main__':
    app.run(debug=True)
