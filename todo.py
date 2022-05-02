
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Köprüyü sqlalchemy ile köprü kurduk

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/es_lo/Desktop/PythonFlaskProject/FlaskTodoApp/todo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# Get 
@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)
 
# Add
@app.route("/add",methods=["POST"])
def add():
    title = request.form.get("todo_title")
    newTodo = Todo(title = title,complete = False)    
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

# status 
@app.route("/complete/<string:id>")
def complete(id):
    todos = Todo.query.filter_by(id=id).first()
    todos.complete = not todos.complete 
    db.session.commit()
    return redirect(url_for("index"))

#delete
@app.route("/delete/<string:id>")
def delete(id):
    todos = Todo.query.filter_by(id=id).first()
    db.session.delete(todos)
    db.session.commit()
    return redirect(url_for("index"))
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)