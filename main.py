from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import random


app = Flask(__name__)
Bootstrap(app)
PLANETS = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune", "Pluto", "Fortune", "Chiron",
           "North-Node", "Vertex"]
SIGNS = ["Ares", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
planet_pairs = []
ascendant_pair = []


# TODO: Create a function that calculates the Ascendant pair
#  (1 house + 1 of 30 degrees)
def get_ascendant():
    house = random.choice(range(1, 13))
    ascendant = random.choice(range(1, 31))
    return {"house": house,
            "ascendant": ascendant
            }


# TODO: Create a function that will generate a degree-sign pair
def gen_planets():
    pairs = []
    for planet in PLANETS:
        degree = random.choice(range(0,30))
        sign = random.choice(SIGNS)
        new_dict = {"name": planet,
                    "degree": degree,
                    "sign": sign
                    }
        pairs.append(new_dict)
    return pairs


@app.route('/')
def home():
    pair = get_ascendant()
    planet_pairs = gen_planets()
    return render_template("index.html", ascendant=pair, planets=planet_pairs)


if __name__ == '__main__':
    app.run(debug=True)
