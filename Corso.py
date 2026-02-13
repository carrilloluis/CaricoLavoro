from __main__ import app, DB, MINIMAL_CORS
import sqlite3
import json
import bottle
from contextlib import closing

@app.route('/v1/Corso/<idx:int>/', method='GET')
def show_c1(idx:int):
	ds_ = {}
	try:
		with sqlite3.connect(DB) as connection_:
			with closing(connection_.cursor()) as cursor_:
				cursor_.row_factory = sqlite3.Row
				cursor_.execute("SELECT [i] AS id, COALESCE([m], '') AS nm FROM [h7mo] WHERE [i]=?", (idx, ))
				ds_ = [dict(r) for r in cursor_.fetchall()]
	except sqlite3.OperationalError as e1:
		return bottle.HTTPResponse(body=json.dumps({'error' : str(e1) }), status=500)
	if len(ds_) > 0:
		return bottle.HTTPResponse(body=json.dumps(ds_), status=200, headers=MINIMAL_CORS)
	else:
		return bottle.HTTPResponse(body={}, status=404)

@app.route('/v1/Corso/__/', method='GET')
def list_c1_2_component():
	ds_ = {}
	try:
		with sqlite3.connect(DB) as connection_:
			with closing(connection_.cursor()) as cursor_:
				cursor_.row_factory = sqlite3.Row
				cursor_.execute("SELECT [i] AS id, COALESCE([m], '') AS nm FROM [h7mo] WHERE (([e] & 1) = 1)")
				ds_ = [dict(r) for r in cursor_.fetchall()]
	except sqlite3.OperationalError as e1:
		return bottle.HTTPResponse(body=json.dumps({'error' : str(e1) }), status=500)
	if len(ds_) > 0:
		return bottle.HTTPResponse(body=json.dumps(ds_), status=200, headers=MINIMAL_CORS)
	else:
		return bottle.HTTPResponse(body={}, status=404)