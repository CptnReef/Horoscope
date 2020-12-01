from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))

@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('index.html')
