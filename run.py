from market import app

"""
This script runs the Flask application defined in the 'market' package.
It imports the 'app' object from the 'market' package and starts the Flask
development server with debugging enabled when executed as the main module.
Usage:
    Run this script directly to start the Flask development server.
Example:
    $ python run.py
Attributes:
    app (Flask): The Flask application instance imported from the 'market' package.
Note:
    Debug mode is enabled for development purposes. Disable debug mode in a
    production environment.
"""
if __name__ == "__main__":
    app.run(debug=True)
