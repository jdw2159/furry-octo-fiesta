from flask import Flask, request, render_template, g, redirect, Response
from sqlalchemy import *
 
app = Flask(__name__)
DATABASEURI = 'postgresql://localhost/sample'
engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request
  The variable g is globally accessible
  """
  try:
  	g.conn = engine.connect()
  except:
  	print "uh oh, problem connecting to database"
  	import traceback; traceback.print_exc()
  	g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/')
def home():
	result = g.conn.execute("SELECT * FROM names;")
	nameList = []
	for row in result:
		nameList.append(row[0])
	return render_template('home.html', name_list=nameList)

@app.route('/add')
def add():
	name = ''
	try:
		name = request.args.getlist('name')[0]
	except:
		a = 1
	if name is not '':
		command = "INSERT INTO names VALUES(%s);"
		args = (name)
		g.conn.execute(command, args)
	return render_template('add.html')
 
if __name__ == '__main__':
	app.run(debug=True)