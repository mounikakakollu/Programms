from flask import Blueprint, render_template, abort, request, jsonify, make_response, Flask
from flask import request
from services import ContentsService
from entites import Contents
from . import api
import pdb
import json
from service import ContentsService

def convert_input_to(class_):
   def wrap(f):
       def decorator(*args):
           pdb.set_trace()
           obj = json.loads(**request.get_json())
           return f(obj)
       return decorator
   return wrap


@api.route('/contents', methods=['POST'])
def create():
    contentsJson = request.json
    contents = ContentsService.createContents(contentsJson)
    if contents:
        return make_response(jsonify(
                {'status': 'success', 'data': contents}
            ), 200)
    else:
        return make_response(jsonify(
                {'status': 'failed', 'message': 'object is not saved'}
            ), 400)

@api.route('/contents', methods=['GET'])
def get():
    contents = ContentsService.getContents()
    if len(contents)>0:
        return make_response(jsonify(
                {'status': 'success', 'data': contents}
            ), 200)
    else:
        return make_response(jsonify(
                {'status': 'failed', 'message': 'data not found'}
            ), 204)
