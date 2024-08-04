from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
import cohere

ai_secret_key = "D7VTCq4nHTJUJAToDVrwKJjCwWyOxATTgZs1bIF7"

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'eebde5e429d4d7d3c6fef4c25467d067a24880a8a5260b3c')

cohere_api_key = os.environ.get(ai_secret_key)
co = cohere.Client(cohere_api_key) if cohere_api_key else None

# Insurance data with URLs
insurance_data = {
    'Company Name': [
        'State Farm', 'Progressive', 'Allianz', 'Nationwide', 'Lemonade', 
        'Esurance', 'Cigna', 'Liberty Mutual', 'Applied Systems', 'Gradient AI',
        'Allstate', 'Geico', 'Farmers', 'USAA', 'Travelers'
    ],
    'Type': [
        'Car', 'Car', 'Health', 'Health', 'Home', 
        'Home', 'Health', 'Car', 'Home', 'Health',
        'Car', 'Car', 'Home', 'Health', 'Home'
    ],
    'Coverage Amount': [
        100000, 200000, 300000, 400000, 500000, 
        600000, 700000, 800000, 900000, 1000000,
        110000, 220000, 330000, 440000, 550000
    ],
    'Premium': [
        500, 1000, 1500, 2000, 2500, 
        3000, 3500, 4000, 4500, 5000,
        550, 1050, 1550, 2050, 2550
    ],
    'URL': [
        'https://www.statefarm.com/', 'https://www.progressive.com/', 'https://www.allianz.com/', 'https://www.nationwide.com/', 'https://www.lemonade.com/', 
        'https://www.esurance.com/', 'https://www.cigna.com/', 'https://www.libertymutual.com/', 'https://www.appliedsystems.com/', 'https://www.gradientai.com/',
        'https://www.allstate.com/', 'https://www.geico.com/', 'https://www.farmers.com/', 'https://www.usaa.com/', 'https://www.travelers.com/'
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = {
            'personalInformation': {
                'firstName': request.form.get('firstName'),
                'lastName': request.form.get('lastName'),
                'age': request.form.get('age'),
                'gender': request.form.get('gender'),
                'contactNumber': request.form.get('contactNumber'),
                'email': request.form.get('email')
            },
            'carInsurance': {
                'vehicleMake': request.form.get('vehicleMake'),
                'vehicleModel': request.form.get('vehicleModel'),
                'vehicleYear': request.form.get('vehicleYear'),
                'vin': request.form.get('vin'),
                'mileage': request.form.get('mileage'),
                'usage': request.form.get('usage')
            },
            'healthInsurance': {
                'healthProvider': request.form.get('healthProvider'),
                'healthCoverage': request.form.get('healthCoverage'),
                'preExistingConditions': request.form.get('preExistingConditions')
            },
            'homeInsurance': {
                'homeAddress': request.form.get('homeAddress'),
                'homeType': request.form.get('homeType'),
                'homeValue': request.form.get('homeValue')
            }
        }
        
        session['form_data'] = json.dumps(form_data)
        session['messages'] = []  # Clear messages when a new form is submitted
        return redirect(url_for('recommendation'))
    except Exception as e:
        app.logger.error(f"Error in submit: {str(e)}")
        return jsonify({"error": f"An error occurred while processing your request: {str(e)}"}), 500

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    form_data = json.loads(session.get('form_data', '{}'))
    messages = session.get('messages', [])
    
    if request.method == 'POST':
        user_message = request.form.get('user_message')
        if user_message:
            messages.append(('user', user_message))
            bot_response = generate_bot_response(user_message, form_data)
            messages.append(('bot', bot_response))
            session['messages'] = messages
    
    return render_template('recommendation.html', form_data=form_data, messages=messages)

def generate_bot_response(user_message, form_data):
    user_message = user_message.lower()
    if 'car' in user_message:
        car_insurances = [
            f"<a href='{url}' target='_blank'>{company}</a> offers car insurance with ${coverage:,} coverage for a premium of ${premium}"
            for company, type, coverage, premium, url in zip(
                insurance_data['Company Name'],
                insurance_data['Type'],
                insurance_data['Coverage Amount'],
                insurance_data['Premium'],
                insurance_data['URL']
            )
            if type.lower() == 'car'
        ]
        return f"Based on your {form_data['carInsurance']['vehicleYear']} {form_data['carInsurance']['vehicleMake']} {form_data['carInsurance']['vehicleModel']}, here are some car insurance options:\n" + "\n".join(car_insurances)
    elif 'health' in user_message:
        health_insurances = [
            f"<a href='{url}' target='_blank'>{company}</a> offers health insurance with ${coverage:,} coverage for a premium of ${premium}"
            for company, type, coverage, premium, url in zip(
                insurance_data['Company Name'],
                insurance_data['Type'],
                insurance_data['Coverage Amount'],
                insurance_data['Premium'],
                insurance_data['URL']
            )
            if type.lower() == 'health'
        ]
        return f"Considering your current health provider is {form_data['healthInsurance']['healthProvider']}, here are some health insurance options:\n" + "\n".join(health_insurances)
    elif 'home' in user_message:
        home_insurances = [
            f"<a href='{url}' target='_blank'>{company}</a> offers home insurance with ${coverage:,} coverage for a premium of ${premium}"
            for company, type, coverage, premium, url in zip(
                insurance_data['Company Name'],
                insurance_data['Type'],
                insurance_data['Coverage Amount'],
                insurance_data['Premium'],
                insurance_data['URL']
            )
            if type.lower() == 'home'
        ]
        return f"For your {form_data['homeInsurance']['homeType']} valued at {form_data['homeInsurance']['homeValue']}, here are some home insurance options:\n" + "\n".join(home_insurances)
    else:
        return "I'm sorry, I didn't understand that. Can you please specify if you'd like to discuss car, health, or home insurance?"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
