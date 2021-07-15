from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/page_start')
def func_page_start():
    conn = sqlite3.connect('dog_db.sqlite')
    c = conn.cursor()

    query = """
    SELECT id, name FROM "dogs";
    """

    c.execute(query)

    dogs_list = c.fetchall()
    conn.close()

    return render_template('index0.html', dogs_list=dogs_list)


@app.route('/breed/<int:index>')
def func_choose_dog(index):

    conn = sqlite3.connect('dog_db.sqlite')
    c = conn.cursor()

    query = """
    SELECT * FROM "dogs" WHERE "id"=?;
    """

    c.execute(query, (index,))

    dog_info = c.fetchall()
    dog = dog_info[0]
    print(dog_info)

    return render_template('dog.html', dog=dog)


@app.route('/add_new_breed')
def add_new_breed():
    return render_template('index1.html')


@app.route('/read_new_breed')
def func_page_b():
    name_backend = request.args.get('name_from_form')
    description_backend = request.args.get('description_from_form')
    character_backend = request.args.get('character_from_form')
    color_backend = request.args.get('color_from_form')
    weight_m_backend = request.args.get('male_weight_from_form')
    weight_f_backend = request.args.get('female_weight_from_form')
    height_m_backend = request.args.get('male_height_from_form')
    height_f_backend = request.args.get('female_height_from_form')
    health_backend = request.args.get('health_from_form')

    return render_template('index2.html', name=name_backend, description=description_backend, character=character_backend, color=color_backend, male_weight=weight_m_backend, female_weight=weight_f_backend, male_height=height_m_backend, female_height=height_f_backend, health=health_backend)


@app.route('/write_new_breed')
def write_new_breed():

    name_backend = request.args.get('name_from_form')
    description_backend = request.args.get('description_from_form')
    character_backend = request.args.get('character_from_form')
    color_backend = request.args.get('color_from_form')
    weight_m_backend = request.args.get('male_weight_from_form')
    weight_f_backend = request.args.get('female_weight_from_form')
    height_m_backend = request.args.get('male_height_from_form')
    height_f_backend = request.args.get('female_height_from_form')
    health_backend = request.args.get('health_from_form')

    #POŁĄCZENIE Z BAZĄ I TAK I SAMO JAK RESZTA
    conn = sqlite3.connect('dog_db.sqlite')
    c = conn.cursor()

    query = """
    INSERT INTO "dogs" VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    c.execute(query, (name_backend, description_backend, character_backend, color_backend, weight_m_backend, weight_f_backend,
                      height_f_backend, height_m_backend, health_backend))
    conn.commit()
    return redirect('/')
    # "'index2.html', name=name_backend, description=description_backend, character=character_backend, color=color_backend, male_weight=weight_m_backend, female_weight=weight_f_backend, male_height=height_m_backend, female_height=height_f_backend, health=health_backend)



if __name__ == '__main__':
    app.run(debug=True)
