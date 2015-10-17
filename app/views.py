from app import app 

@app.route('/')
def index():
	return "Hello World!"

@app.route('/lessons')
def lessons():
	return "Here, there will be the lessons"
