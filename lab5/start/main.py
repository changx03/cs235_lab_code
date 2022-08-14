"""Web server entry point.

Note: 
Since we have defined all environment variables, we do NOT call `app.run()` and 
`python main.py` will not run the Flask server.
"""

from app import create_app

app = create_app()
