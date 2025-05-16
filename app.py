from flask import Flask, request, make_response, redirect, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    user_ip_information = request.remote_addr
    return f"Hola Como estas tu direccion IP es: {user_ip_information}"

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_url"))
    response.set_cookie("user_ip_information", user_ip_information)
    return response

@app.route("/show_url")
def show_url():
    user_ip = request.cookies.get("user_ip_information")
    return f"Hola Esta es la información redirigida desde cookie: {user_ip}"

items = [
    {"name": "Aple", "price": 10},
    {"name": "Microsof", "price": 20},
    {"name": "Windows", "price": 30},
    {"name": "Linux", "price": 40},
    {"name": "Python", "price": 50},
    ]

@app.route("/show_address")
def show_url_address():
    user_ip = request.cookies.get("user_ip_information")
    context = {
        "user_ip": user_ip,
        "items":items    
    }
    return render_template("index.html", **context)

@app.route("/page")
def page():
    response = make_response(render_template("index.html"))
    response.headers["X-Parachutes"] = "parachutes are cool"
    return response  # Aquí devuelves la respuesta correctamente
    
app.run(host='0.0.0.0', port=3000, debug=True)