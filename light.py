from flask import Flask, request, render_template, json


app = Flask(__name__)

@app.route("/light",  methods=['GET', 'POST'])
def light():
    if request.method == "POST":
        results = request.form
        with open('static/file.json', 'w') as f:
           json.dump(request.form, f)
    return render_template('form.html')

app.run(debug=True, use_reloader=False)
