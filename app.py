from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for main DigiCard page
@app.route('/')
def main():
    return render_template('main.html')

# Route for agritech page
@app.route('/agritech')
def agritech():
    return render_template('agritech.html')

# Route for dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for documents page
@app.route('/documents')
def documents():
    return render_template('documents.html')

# Route for login page (GET and POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        password = request.form['password']
        # Add your validation logic here
        # Example validation (replace with your logic)
        if aadhar == "123456789012" and password == "password123":
            return redirect(url_for('dashboard'))  # Redirect to dashboard on successful login
        else:
            error = "Invalid Aadhar number or password."
            return render_template('login.html', error=error)  # Return to login with error
    return render_template('login.html')  # Return login page for GET request

# Route for profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Route for register page
@app.route('/register')
def register():
    return render_template('register.html')

# Route for services page
@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)
