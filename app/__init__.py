from flask import Flask

# crear el objeto principal
app = Flask(__name__)

#import a las rutas definidas 
from app import routes

if __name__ == "__main__":
    app.run()