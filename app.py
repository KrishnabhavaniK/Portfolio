from flask import Flask, render_template

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Skills Page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Route for Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
