from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_page():
   """Handle adding a and b"""
   a = int(request.args.get('a'))
   b = int(request.args.get('b'))
   result = add(a,b)
   return str(result)


@app.route('/sub')
def sub_page():
   """Handle subtracting a and b"""
   a = int(request.args.get('a'))
   b = int(request.args.get('b'))
   result = sub(a,b)
   return str(result)


@app.route('/mult')
def mult_page():
   """Handle multiplying a and b"""
   a = int(request.args.get('a'))
   b = int(request.args.get('b'))
   result = mult(a,b)
   return str(result)


@app.route('/div')
def div_page():
   """Handle dividing a and b"""
   a = int(request.args.get('a'))
   b = int(request.args.get('b'))
   result = div(a,b)
   return str(result)


operators = {
   'add': add,
   'sub': sub,
   'mult': mult,
   'div': div
   }
@app.route('/math/<oper>')
def all_in_one(oper):
   """Handle all four math operations for parameters a & b"""

   a = int(request.args.get('a'))
   b = int(request.args.get('b'))
   result = operators[oper](a,b)
   return str(result)
   