from flask import Flask, request
from time import gmtime, strftime

app = Flask(__name__)

@app.route('/')
def hello_world():
    ip_addr = request.remote_addr
    cur_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return f"Hello World!<br>\n Its {cur_time} and your IP is {ip_addr}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
