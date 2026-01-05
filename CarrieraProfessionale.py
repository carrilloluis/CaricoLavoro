from __main__ import app, DB, MINIMAL_CORS
import sqlite3
import json
import bottle
from contextlib import closing

@app.route('/v1/CarrieraProfessionale/<idx:int>/', method='GET')
def show_cp(idx:int):
	ds_ = {}
	str_show = """
		SELECT [i] AS id, COALESCE([a], '') AS nm 
		FROM [t2] 
		WHERE [i]=?
		"""
	try:
		with sqlite3.connect(DB) as connection_:
			with closing(connection_.cursor()) as cursor_:
				cursor_.row_factory = sqlite3.Row
				cursor_.execute(str_show, (idx, ))
				ds_ = [dict(r) for r in cursor_.fetchall()]
	except sqlite3.OperationalError as e1:
		return bottle.HTTPResponse(body=json.dumps({'error' : str(e1) }), status=500)
	if len(ds_) > 0:
		return bottle.HTTPResponse(body=json.dumps(ds_), status=200, headers=MINIMAL_CORS)
	else:
		return bottle.HTTPResponse(body={}, status=404)

@app.route('/v1/CarrieraProfessionale/__/', method='GET')
def list_cp():
	ds_ = {}
	str_list = """
		SELECT [i] AS id, COALESCE([a], '') AS nm
		FROM [t2] 
		WHERE (([f] & 1) = 1)
		"""
	try:
		with sqlite3.connect(DB) as connection_:
			with closing(connection_.cursor()) as cursor_:
				cursor_.row_factory = sqlite3.Row
				cursor_.execute(str_list)
				ds_ = [dict(r) for r in cursor_.fetchall()]
	except sqlite3.OperationalError as e1:
		return bottle.HTTPResponse(body=json.dumps({'error' : str(e1) }), status=500)
	if len(ds_) > 0:
		return bottle.HTTPResponse(body=json.dumps(ds_), status=200, headers=MINIMAL_CORS)
	else:
		return bottle.HTTPResponse(body={}, status=404)