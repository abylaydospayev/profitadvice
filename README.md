# Insurance Recommendation System

## Project Overview
This project is an Insurance Recommendation System that uses Flask to serve a web application. It provides personalized insurance recommendations based on user input and leverages an AI API for intelligent chat interactions.

## Features
- User-friendly web interface for inputting personal and insurance-related information
- Personalized insurance recommendations for car, health, and home insurance
- Interactive chat system powered by AI for dynamic user interactions
- Responsive design using Bootstrap for optimal viewing on various devices

## Technologies Used
- Backend: Python, Flask
- Frontend: HTML, CSS (Bootstrap), JavaScript
- AI Integration: Cohere API
- Database: [Specify if you're using any database]


## Setup and Installation
1. Clone the repository:
git clone [repository-url]
cd insurance_recommendation
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\act

3. Install the required packages:
   pip install -r requirements.txt


4. Set up environment variables:
- Create a `.env` file in the root directory
- Add your Cohere API key:
  ```
  COHERE_API_KEY=your_api_key_here
  ```

5. Run the application:
python app.py


6. Open a web browser and navigate to `http://localhost:5000`

## Usage
1. Navigate to the home page and click on "Get Advice"
2. Fill out the form with your personal and insurance-related information
3. Submit the form to receive personalized insurance recommendations
4. Use the chat interface to ask questions and receive AI-powered responses

## AI Integration
This project uses the Cohere API for generating intelligent responses in the chat system. Ensure you have a valid API key and have set it in the environment variables.


## Contact
Abylay Dospayev
abylaidospayev@gmail.com



