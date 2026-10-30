from database.exts import db

# Define the User database model using Flask-SQLAlchemy (inherits from db.Model)
class User(db.Model):
    # Unique primary key integer for each user record
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False)
    department = db.Column(db.String(), nullable = False)
    designation = db.Column(db.String(), nullable = False)
    contact = db.Column(db.String(), nullable  = False)
    # User role/permissions (mandatory field)
    role = db.Column(db.String(), nullable = False)
    # ID of the user's manager (mandatory field)
    manager_id = db.Column(db.Integer(), nullable = False)

# Helper function to add and commit a new record to the database session
def save(self):
    db.session.add(self)
    db.session.commit()

# Helper function to delete an existing record from the database session
def delete(self):
    db.session.delete(self)
    db.session.commit()

# Helper function to update an existing user's field values and commit the changes
def update(self, name, email, department, designation, contact, role, manager_id):
    self.name = name
    self.email = email
    self.department = department
    self.designation = designation
    self.contact = contact
    self.role = role
    self.manager_id = manager_id

    db.session.commit()

