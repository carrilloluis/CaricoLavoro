import bottle
import os

__author__ = 'Luis Carrillo Gutiérrez'
__copyright__ = "Copyright 2020, Luis Carrillo Gutiérrez"

app = bottle.Bottle()

DB = '/tmp/data.db'

MINIMAL_CORS = {
	'Content-type':'application/json',
	'Access-Control-Allow-Origin':'*',
	'Access-Control-Allow-Methods':'GET, POST, OPTIONS, PUT, PATCH, DELETE',
	'Access-Control-Allow-Headers':'*'
}

import PeriodoAccademico
# import Corso
# import CarrieraProfessionale
# import Insegnante
# import CaricoDiLavoro

@app.error(404)
def errore404(error):
	return bottle.HTTPResponse(body={}, status=404)

@app.route('/', method='GET')
def ui():
	return bottle.static_file("./index.html", root='./UI/')

@app.route("/js/<filepath:re:.*\.(js|mjs)>", method='GET')
def assets_(filepath):
	return bottle.static_file(filepath, root='./UI/js/')

@app.route("/css/<filepath:re:.*\.css>", method='GET')
def assets_css(filepath):
	return bottle.static_file(filepath, root='./UI/css/')

if __name__ == "__main__":
	HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '60101'))
	except ValueError:
		PORT = 60101
	app.run(host=HOST, port=PORT, reloader=True, debug=True)
