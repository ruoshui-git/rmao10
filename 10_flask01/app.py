# Ruoshui -- pending group review
# SoftDev -- Rona Ed.
# Oct 2020 

from flask import Flask, render_template
import occupations

app = Flask(__name__) #create instance of class Flask

TNPG = "Team Nine2One"
ROSTER = "Julianna Yu, Cindy Zheng, Ruoshui Mao"

@app.route("/")       #assign fxn to route
def index():
    context = {
        'tnpg': TNPG,
        'roster': ROSTER,
        'occupations': occupations.names,
        'chosen': occupations.get_random(),
    }
    return render_template('./index.html', **context)


if __name__ == "__main__":  # true if this file NOT imported
    app.run(debug=True)