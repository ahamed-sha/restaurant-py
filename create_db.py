# all the imports
import sqlite3
from contextlib import closing
import json
from flask import Flask, jsonify, request, Response, Request, render_template

# configuration
DATABASE = './data.db'
DEBUG = True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('./schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()


def connect_db():
  return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
  init_db()

