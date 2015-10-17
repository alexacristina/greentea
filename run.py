from app import app
from flask_bootstrap import Bootstrap


def run():
	app.run(debug=True)

if __name__ == "__main__":
	run()
