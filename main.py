from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def indexp():
    return render_template('index.html')


@app.route("/light",  methods=['GET', 'POST'])
def light():
    if request.method == "POST":
        results = request.form
        with open('static/file.json', 'w') as f:
           json.dump(request.form, f)
    return render_template('form.html')

@app.route("/PA")
def pasys():
    url = "http://www.srmuniv.ac.in/sites/all/themes/srmuniversity/main_layout/images/menu-img2.jpg"

    return render_template('PA.html', var="123")


app.run(debug=True, use_reloader=False)
