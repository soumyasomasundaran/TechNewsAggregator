from logging import debug

from flask import Flask
from tnaggregator import app

if __name__ == '__main__':
    app.run(debug = True)