from flask import Flask
app = Flask(__name__)

from flask import render_template, url_for, flash, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

app.config['SECRET_KEY']='bbe5e3b13618b036790dd5669e35137a'

class url(FlaskForm):
	url=StringField("Enter url", validators=[DataRequired(), URL()])
	submit=SubmitField("Enter")

@app.route("/")
@app.route("/input", methods=['GET', 'POST'])
def register():
	form = url()
	if request.method == 'POST':
		if form.validate() == False:
		# flash('All fields are required.')
			return render_template('input.html', form = form)
		else:
			Url = form.url.data
			from Prediction import output
			ans = output(Url)
			return render_template('success.html',title = ans)
	elif request.method == 'GET':
		return render_template('input.html', form = form)

if __name__ == '__main__':
	app.debug = True
	app.run()

# Used https://www.tutorialspoint.com/flask/flask_wtf.htm