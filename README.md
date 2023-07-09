# OAuth2 

Flask OAuth2 with Auth0 and Gmail Integration

## Description

This is a Flask application that uses OAuth2 protocol to authenticate users via Auth0. It supports login via Gmail and stores user's profile information in a session, such as nickname and picture URL. The user data is then used to customize the dashboard and a new settings page.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or later
- Flask
- Authlib
- python-dotenv

You can install the necessary packages with pip:

```
pip install flask authlib python-dotenv
```

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/flask-oauth.git
   ```

2. Navigate to the project directory:
   ```
   cd flask-oauth
   ```

3. Create a `.env` file in the project root and add your Auth0 application credentials (this is mandatory for the application to run):
   ```
   SECRET_KEY=your_secret_key
   ```

4. Finally, run the application:
   ```
   python app.py
   ```

The application will run on `http://localhost:8000`

## Usage

1. Open your web browser and visit `http://localhost:8000/home`
2. Click on the login button to authenticate via Auth0
3. Login using your Gmail credentials
4. You will be redirected to the dashboard after successful authentication
5. From the dashboard, navigate to the settings page where you will find the user's nickname stored in the session and the picture obtained from the JSON response object.

## Development

The main application is contained within `app.py`. User data is stored in a session after the OAuth2 process is completed.

- The `@app.route('/dashboard')` route displays the user's dashboard after a successful login.
- The `@app.route('/settings')` route is a new protected route where the user's nickname is stored in a session variable.
- The `settings.html` is a new view displayed on the `/settings` route where the picture from the JSON object is loaded.

The `@request_auth` decorator is used to protect routes that require authentication.

## Demo Video

A demo video of the functionality can be found at the following [link](#).

## References

- For more information about using Auth0 with Node.js and Express, follow this [link](https://www.infoworld.com/article/3629129/how-to-use-auth0-with-nodejs-and-express.html?page=2).

## Note

This assignment is graded based on effort, not completion. So, don't worry if you didn't manage to get everything working perfectly. The goal is to learn and progress.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
