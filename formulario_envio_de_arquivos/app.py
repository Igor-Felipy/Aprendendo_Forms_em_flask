from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/send', methods=['GET', 'POST'])
def catch_arch():
    if request.method=="POST":
        doc = request.form["data"]
        data = open(doc, "r")
        return render_template('dados.html', data=data)
    
    return render_template('index.html')
    



if __name__=="__main__":
    app.run(debug=True)