from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    title='Mario Gutierrez'
    return render_template('index.html',title=title)

@app.route('/formacion')
def formacion():
    return render_template("formacion.html")

@app.route('/proyectos')
def proyectos():
    return render_template("proyectos.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

if __name__ =='__main__':
    app.run(debug=True, port=4000)