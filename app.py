from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "supersecretkey"

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Upload page route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Logic to handle file upload
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        material_type = request.form['material_type']
        professor = request.form['professor']
        
        # Here you would handle saving the uploaded file and data to a database
        
        flash('Course material uploaded successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('upload.html')

# Search page route
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Logic to handle course search
        course_code = request.form['course_code']
        
        # Here you would check if the course exists in the database
        # If it doesn't, you could show a message or link to files

        flash('No materials found for this course.', 'info')
        return render_template('search.html')
    
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
