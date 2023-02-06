
from app import app
from flask import render_template, make_response, request
from collections import deque
from app.models import db, Classroom

stack = deque()
@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/about')
def about():
    return render_template("/about.html")



#Task1

@app.route('/api/push/<value>', methods = ['GET', 'POST'])
def push(value):
    if value.isdigit():
        val = int(value)
        stack.append(val)
        return make_response(f"Successfully pushed {val} to the stack !", 200)
    else:
        return make_response(f"not pushed to stack!")

@app.route('/api/pop', methods = ['PUT', 'GET'])
def put():
    if stack:
        x = stack[-1]
        stack.pop()
        return f"{x} is popped"
    else:
        return f"Stack is empty!!"

@app.route('/api/view', methods= ['GET'])
def read():
    
    return f"{stack}Successfully printed the stack!!"


#Task 2

@app.route('/api/note/<Serial>/<Name>/<Roll_no>/<Dept>', methods = ['POST', 'GET', 'PUT'])
def funAdd(Serial,Name, Roll_no, Dept):
    to_add = Classroom(serial_no=Serial,name = Name, roll_no = Roll_no, department = Dept)
    db.session.add(to_add)
    db.session.commit()
    return make_response(f"{Name}, {Roll_no}, {Dept} has been successfully added to the database !!")


@app.route('/api/note/<Serial>', methods = ['GET', 'DELETE'])
def funExtract(Serial):
    if request.method == 'GET':
        if Serial.isdigit():
            Serial = int(Serial)
            data = Classroom.query.filter_by(serial_no = Serial).first()
            db.session.commit()
            if data is not None:
                return f"{data.serial_no} . {data.name}, {data.roll_no}, {data.department}"
            else:
                return make_response("no data exists!!")
    elif request.method =='DELETE':
        if Serial.isdigit():
            Serial = int(Serial)
            data = Classroom.query.filter_by(serial_no = Serial).first()
            if data is not None:
                db.session.delete(data)
                db.session.commit()
                return make_response(f"{data.serial_no}, {data.name}, {data.roll_no}, {data.department}  has been deleted!!")
            else:
                return make_response(f"data is not found")
        else:
            return make_response(f"kya hai ye!!")

# @app.route('/api/note/<Serial>/<Name>/<Roll_no>/<Dept>', methods = ['POST', 'GET', 'PUT'])
# def funUpdate(Serial,Name, Roll_no, Dept):
#     if request.method == 'PUT':
#         if Serial.isdigit():
#             Serial = int(Serial)
#             data = Classroom.query.filter_by(serial_no = Serial).first()
#             data.name = Name
#             data.roll_no = Roll_no
#             data.department = Dept
#             db.session.commit()
#             return make_response(f"{data.serial_no} is updated to {data.name}, {data.roll_no}, {data.department}")
#         else:
#             return make_response(f"Serial number is not a digit!!")
#     else:
#         return make_response(f"put nahi ho rha bhaiii!!")


