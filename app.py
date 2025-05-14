from flask import Flask, request, jsonify #Import request and jsonify
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database
# 'sqlite:///site.db' means a SQLite database file named 'site.db' in the same directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# This is to suppress a warning; 
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary key, auto-increments
    name = db.Column(db.String(100), nullable=False) # Employee name, cannot be empty
    department = db.Column(db.String(50), nullable=False) # Employee department
    
    gender = db.Column(db.String(20)) #Using String for gender
    age = db.Column(db.Integer) #Using Integer for age

    # This method helps when printing Employee objects
    def __repr__(self):
        return f"Employee('{self.name}','{self.department}','{self.gender}','{self.age}')"

# --- New Route to Get, Update, or Delete a Specific Employee ---
# This route includes a variable part: <int:employee_id>
@app.route('/employees/<int:employee_id>',methods=['GET','PUT','DELETE']) #We'll the add PUT and DELETE later
def handle_employee(employee_id):
    # Logic to get a specific employee
    employee = Employee.query.get(employee_id) #Query the database for an employee by their primary key (id)
    
    if employee is None:
        # If no employee is found with that ID, return a 404 Not Found error
        return jsonify({'error': 'Employee not found'}), 404
    
    if request.method == 'GET':
        # if the employee is found, return their details as JSON
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'department':employee.department,
            'gender': employee.gender,
            'age': employee.age
        })
        
    elif request.method == 'PUT':
        # Logic the update an employee
        data = request.get_json() # Get Json data from the request body
        
        # Update employee attributes based on provided data
        if 'name' in data:
            employee.name = data['name']
        if 'department' in data:
            employee.department = data['department']
        if 'gender' in data:
            employee.gender = data['gender']
        if 'age' in data:
            employee.age = data['age']
            
        db.session.commit() # Commit the changes to the database
        
        return jsonify({'message': 'Employee updated successfully!'}) # Return success message
    
    elif request.method == 'DELETE':
        # Logic to delete an employee
        db.session.delete(employee) # Delete the employee object
        db.session.commit() # Commit the changes
        
        return jsonify({'message': 'Employee deleted successfully!'}) #Return success manage, or 204 No Content is also common
            
# --- End New Route ---

# --- New Route for Employees API ---
@app.route('/employees', methods=['GET','POST']) #Specify allowed HTTP methods
def handle_employees():
    if request.method == 'POST':
        
        data = request.get_json() # Get JSON data from the request body
        
        if not data or not data.get('name') or not data.get('department'):
            
            return jsonify({'error': 'Name and Department are required'}), 400
        
        new_employee = Employee(
            name = data['name'],
            department = data['department'],
            gender = data.get('gender'),
            age = data.get('age')
        )
        
        db.session.add(new_employee) # Add the new employee to the database session
        db.session.commit() # Commit the session to save the data
        
        return jsonify({'message': 'Employee added successfully!', 'id': new_employee.id}),201
    
    elif request.method == 'GET':
        #Logic to get all employees
        employees = Employee.query.all() #Query all employee records from the database
        # Convert the list of Employee objects into a list of dictinaries for json response
        employees_list = []
        for employee in employees:
            employees_list.append({
                'id':employee.id,
                'name':employee.name,
                'department':employee.department,
                'gender': employee.gender,
                'age': employee.age
            })
        return jsonify(employees_list) # Return the list as a JSON response

# --- End New Route ---

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Hello, Flask!'

# Run the application
if __name__ == '__main__':
    #Before running the app, create the database tables based on the models
    with app.app_context():
        db.create_all()
    app.run(debug=True)