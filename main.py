import io
import json

from flask import  Flask
from activity import *


activeList = AcitivyList([])


app = Flask(__name__)

@app.route('/')
def index():
  """
  docstring
  """
  activeList.initialize_me()
  with io.open('activities.json', 'w', encoding='utf8') as json_file:
    data = json.dumps(activeList.serialize(), indent=4, sort_keys=True)
    return data


@app.route('/hello')
def hello():
  """
  docstring
  """
  return 'Hey there Newcomer!'
