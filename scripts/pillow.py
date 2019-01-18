import hug
import time
from datetime import datetime
from falcon import HTTP_201


@hug.get('/anything/#')
def get_sharpe():
    return {"result": "accepted sharp"}

@hug.get('/anything/%23')
def get_sharpe():
    return {"result": "accepted %23"}

