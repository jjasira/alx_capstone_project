from config import app, db
from dotenv import load_dotenv, dotenv_values
from email.message import EmailMessage
from flask import request, jsonify
from models import Contact
import os
import smtplib
import ssl

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()

    """since the contacts that have been retirieved is a list of Contact objects, the to_json method will convert them to json using the generator below"""
    json_contacts = list(map(lambda x:x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    """we get the firstname, lastname and email address from our frontend"""
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    
    """We get the email sender's details from our environment variables"""
    email_sender = os.getenv('EMAIL_SENDER2')
    email_password = os.getenv('PASSWORD')

    """This is the email that will receive the details of the new subscriber from our server"""
    email_receiver = "jjasira2018@gmail.com"
    """The email sunject"""
    subject = "New Subscription"
    """The email body"""
    body = f"{first_name} {last_name} subscribed to your newsletter with {email}"

    """initialize our email object and set the parameters"""
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        """Login to the email address and send email"""
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


    """Validate that every field required is entered"""
    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name and email"}), 400
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        """add to the database session"""
        db.session.add(new_contact)
        """commit the changes"""
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created"}), 201

 
@app.route('/update_contact/<int:user_id>', methods=['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.enail = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated"}), 200

@app.route('/delete_contact/<int:user_id>)', methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    """prevents this code from running when imported from another script"""
    with app.app_context():
        """get the context of the application before creating all the models that have been initialized from the models file"""
        db.create_all()

    app.run(debug=True)