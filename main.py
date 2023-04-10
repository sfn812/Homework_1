from flask import Flask
import func_receiving_data

app = Flask(__name__) # Creature instance приложения

@app.route("/")
def index():
    result = ""
    canditates = func_receiving_data.get_all()

    for canditate in canditates:
        result += canditate["name"] + "<br>"
        result += canditate["position"] + "<br>"
        result += canditate["skills"] + "<br>"
        result += "<br>"


    return f"<pre> {result} </pre> "


@app.route("/pk/<int:pk>")
def canditates_pk(pk):
    result = ""
    canditate = func_receiving_data.get_by_pk(pk)

    if canditate == "Not found":
        return canditate


    result += canditate["name"] + "<br>"
    result += canditate["position"] + "<br>"
    result += canditate["skills"] + "<br>"

    print(canditate['picture'])


    return f"""<img src={canditate['picture']}>
    <pre> {result}  </pre>"""

@app.route("/skills/<skill>")
def canditates_skills(skill):
    result = '<br>'
    canditates = func_receiving_data.get_by_skill(skill)

    for canditate in canditates:
        result += canditate["name"] + "<br>"
        result += canditate["position"] + "<br>"
        result += canditate["skills"] + "<br>"
        result += "<br>"

    return f'<pre> {result}  </pre>'






app.run(debug=True) # debug=True отображает наши ошибки

