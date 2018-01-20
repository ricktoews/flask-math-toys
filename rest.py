import sys
sys.path.append('./math_toys')

from flask import Flask

from math_toys import tri
from math_toys import phi

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/tri/<int:n>")
def nth_tri(n):
	_tri = str(tri.nth_tri(n))
	return _tri

@app.route("/n_tris/<int:n>")
def first_n_tris(n):
	_tris = str(tri.first_n_tris(n))
	return _tris

@app.route("/phi/<int:n>")
def nth_phi(n):
	_phi = str(phi.nth(n))
	return _phi

@app.route("/n_phis/<int:n>")
def first_n_phis(n):
	_phis = str(phi.first_n(n))
	return _phis
