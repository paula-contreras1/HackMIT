from flask import Flask, render_template, url_for 

app = Flask(__name__)

posts = [
	{
		'author': 'Lorem Ipsum',
		'title' : 'Blog Post 1',
		'content' : 'Connect via API',
		'date_posted' : 'Date'
	
	},
	{
		'author': 'Lorem Ipsum',
		'title' : 'Blog Post 1',
		'content' : 'Connect via API',
		'date_posted' : 'Date'

	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = posts) 

@app.route('/about')
def about():
	return render_template('about.html', title= 'about') 


if __name__ == '__main__':
	app.run(debug=True)
