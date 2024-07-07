from flask import Flask, render_template, request, session
from procesare import gasire_combinatii


app = Flask(__name__, template_folder='templates')


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', "GET"])

def result():
    output = request.form.to_dict()
    wanted_cal = output["wanted_cal"]
    res = gasire_combinatii(int(wanted_cal))
    return render_template("index.html", res=res)


if __name__ == '__main__':
    app.run(debug = True, port = 5001)
