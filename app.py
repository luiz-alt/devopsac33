import os
from flask import Flask, jsonify, request

fibo = Flask(__name__)

@fibo.route('/')
def fibon():
    p = 1
    a = 0
    r = "0,"
 
    for i in range(51):
        tmp = p
        p = p + a
        a = tmp
        r += str(p) + ","
    return r

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    fibo.run(host='0.0.0.0', port=port)
        