from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def calculate_results(results):
    # Grab each variable:
    age = int(results.get('age', 0))
    num_occupants = int(results.get('num_occupants', 0))
    have_ouija = results.get('have_ouija', "off")
    doors_open = results.get('doors_open', "off")
    hear_children = results.get('hear_children', "off")
    have_basement = results.get('have_basement', "off")
    hear_sounds = results.get('hear_sounds', "off")
    someone_died = results.get('someone_died', "off")

    # Calculate the score
    score = 0
    score += int(age/10)
    score += int(num_occupants/5)
    if have_basement != "on":
        return "You need a basement to play this game!"
    if have_ouija == "on": score += 5
    if hear_children == "on": score += 8
    if doors_open == "on": score += 3
    if hear_sounds == "on": score += int(10-(age/10)) # If the home is new you shouldnt be hearing sounds
    if someone_died == "on": score += 20

    return score

def determine_haunt(score):
    if score == "You need a basement to play this game!":
        return score
    if score < 10:
        return "Not Haunted"
    elif score < 20:
        return "Possibly Haunted"
    elif score < 30:
        return "Probably Haunted"
    else:
        return "Definitely Haunted"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        results = None
        return render_template('index.html')
    else:
        results = request.form
        print(results)
        # Calculate the results
        haunt_score = calculate_results(results)
        haunt_score = determine_haunt(haunt_score)
        return render_template('index.html', haunt_score=haunt_score)


