from flask import render_template, url_for, flash, redirect
from main import app, db
from main.models import Body, Power
from main.forms import CreateBodybuilding, CreatePowerlifting


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/MyPrograms')
def myPrograms():
    bbprograms = Body.query.all()
    plprograms = Power.query.all()
    return render_template('programs.html', bbprograms=bbprograms, plprograms=plprograms)

@app.route('/CreateProgram')
def createProgram():
    return render_template('create.html')

@app.route('/CreateProgram/body-building', methods=["GET", "POST"])
def bodyBuilding():
    form = CreateBodybuilding()
    if form.validate_on_submit():
        program = Body(title=form.title.data, age=form.age.data, gender=form.gender.data, benchMax=form.benchMax.data, squatMax=form.squatMax.data, deadliftMax=form.deadliftMax.data)
        db.session.add(program)
        db.session.commit()
        flash('Program succesfully created')
        return redirect(url_for('myPrograms'))
    #form is instance of create object in forms.py, and passed into the html file
    return render_template('bodybuilding.html', form=form)

@app.route('/CreateProgram/power-lifting', methods=["GET", "POST"])
def powerLifting():
    form = CreatePowerlifting()
    if form.validate_on_submit():
        program = Power(title=form.title.data, age=form.age.data, gender=form.gender.data, benchMax=form.benchMax.data, squatMax=form.squatMax.data, deadliftMax=form.deadliftMax.data)
        db.session.add(program)
        db.session.commit()
        flash('Program succesfully created')
        return redirect(url_for('myPrograms'))

    return render_template('powerlifting.html', form=form)

@app.route('/MyPrograms/<int:bbprogram_id>')
def bbprograms(bbprogram_id):
    program = Body.query.get_or_404(bbprogram_id)
    return render_template('bbprogram.html', program=program) 

@app.route('/MyPrograms/<int:plprogram_id>')
def plprograms(plprogram_id):
    program = Power.query.get_or_404(plprogram_id)
    return render_template('plprogram.html', program=program)


