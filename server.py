from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
   return render_template('index.html')
   
@app.route('/play/<int:num>')
def another_index( num):
   return render_template("hello.html",num=num)

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
   return render_template("colors.html",num=num, color=color)

if __name__ == "__main__":
   app.run(debug = True)

