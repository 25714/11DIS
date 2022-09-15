from FlaskApp1 import app
from flask import render_template, request
from FlaskApp1.cutcut import cutgame
from FlaskApp1.Romannumerals import RomanNumerals
from FlaskApp1.isomorphicpairs import isomorphise
from FlaskApp1.forms import RomanForm, PSRLSForm, IsomorphForm




###################
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # return "<h1>Hello Everyone!!</h>"
    return render_template("index.html", login=False, index=True)

# @app.route("/api/")
# @app.route("/api/<idx>")
# def api(idx = None):
#     if (idx == None):
#         jdata = coursesData
#     else:
#         jdata = coursesData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="FlaskApp1/json")

@app.route("/romannumerals", methods=['GET', 'POST'])
def roman():
    number = ""
    numeral = ""
    form = RomanForm()
    if form.validate_on_submit():
        number = int(request.form.get("roman"))
        if 1 <= number <= 3999:
            numeral = RomanNumerals(number)
        else:
            number = ""
    return render_template("romannumerals.html", romannumerals=True, form=form, title="Roman Numerals", number=number,
                           numeral=numeral)

@app.route("/cutrock", methods=['GET', 'POST'])
def cutrock():
    form = PSRLSForm()
    answer = ""
    result = ""
    if form.paper.data:
        answer = "paper"
        result = cutgame("paper")
    if form.scissors.data:
        answer = "scissors"
        result = cutgame("scissors")
    if form.rock.data:
        answer = "rock"
        result = cutgame("rock")
    if form.lizard.data:
        answer = "lizard"
        result = cutgame("lizard")
    if form.spock.data:
        answer = "spock"
        result = cutgame("spock")

    return render_template("cutrock.html", cutrock=True, form=form, answer=answer, result=result, title="Paper Scissors Rock Lizard Spock")

@app.route("/isomorph", methods=['GET', 'POST'])
def isomorph():
    form = IsomorphForm()
    result = ""
    if form.validate_on_submit():
        string1 = isomorphise(request.form.get("string1").lower())
        string2 = isomorphise(request.form.get("string2").lower())
        if string1 == string2:
            result = f"{request.form.get('string1')} and {request.form.get('string2')} are isomorphic pairs with the pattern {string1}."
        elif len(request.form.get("string1")) != len(request.form.get("string2")):
            result = f"{request.form.get('string1')} and {request.form.get('string2')} are not the same length, and therefore are not isomoprhic pairs."
        else:
            result = f"{request.form.get('string1')} and {request.form.get('string2')} are not isomorphic pairs."
    return render_template("isomorphs.html", isomorphs=True, form=form, result=result, title="Isomorphic Pairs")


