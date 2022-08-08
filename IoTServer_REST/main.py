import pyfirmata
import time

# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import pyfirmata

app = Flask(__name__)
global temps, acts, heats, cools, minTs, maxTs
temps = []
acts = []
heats = []
cools = []
minTs = []
maxTs = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "blablabla"
        return jsonify({'ARDUINO API': data})

@app.route('/temp/<int:temperature>', methods=['GET','PUT'])
def disp(temperature):
    temperature = temperature/100
    if (request.method == 'GET'):
        print('TEMP GET method called')
        return jsonify({'temperature_values': temps[-1]})
    elif (request.method == 'PUT'):
        temps.append(temperature)
        print("TEMP PUT method called")
    return jsonify({'result': 'success you put the value somewhere wohooo'})

@app.route('/act/<int:steps>', methods=['GET','PUT'])
def act(steps):
    if (request.method == 'GET'):
        print('ACT GET method called')
        return jsonify({'activity_values': acts[-1]})
    elif (request.method == 'PUT'):
        acts.append(steps)
        print("ACT PUT method called")
    return jsonify({'result': 'success you put the value somewhere wohooo'})

@app.route('/heat/<int:heat>', methods=['GET','PUT'])
def heat(heat):
    if (request.method == 'GET'):
        print('HEAT GET method called')
        return jsonify({'heat_values': heats[-1]})
    elif (request.method == 'PUT'):
        if heat == 1:
            heat = True
        else:
            heat = False
        heats.append(heat)
        board = pyfirmata.Arduino('com4')
        print(board)
        if heat == True:
            board.digital[13].write(1)
        elif heat == False:
            board.digital[13].write(0)
        board.exit()
        print("HEAT PUT method called")
    return jsonify({'result': 'success you put the value somewhere wohooo'})

@app.route('/cool/<int:cool>', methods=['GET','PUT'])
def cool(cool):
    if (request.method == 'GET'):
        print('COOL GET method called')
        return jsonify({'cool_values': cools[-1]})
    elif (request.method == 'PUT'):
        if cool == 1:
            cool = True
        else:
            cool = False
        cools.append(cool)
        board = pyfirmata.Arduino('com4')
        print(board)
        if cool == True:
            board.digital[12].write(1)
        elif cool == False:
            board.digital[12].write(0)
        board.exit()
        print("COOL PUT method called")
    return jsonify({'result': 'success you put the value somewhere wohooo'})


@app.route('/minT/<int:mint>', methods=['GET','PUT'])
def mint(mint):
    if (request.method == 'GET'):
        print('MINT GET method called')
        return jsonify({'minT_values': minTs[-1]})
    elif (request.method == 'PUT'):
        minTs.append(mint)
        print("MINT PUT method called")
    return jsonify({'result': 'success you put the value somewhere wohooo'})

@app.route('/maxT/<int:maxt>', methods=['GET','PUT'])
def maxt(maxt):
    if (request.method == 'GET'):
        print('MAXT GET method called')
        return jsonify({'maxT_values': maxTs[-1]})
    elif (request.method == 'PUT'):
        maxTs.append(maxt)
        print("MAXT PUT method called")
    return jsonify({'result': 'success you put the value somewhere wohooo'})

'''
        board = pyfirmata.Arduino('com4')
        print(board)
        if temperature==1:
            board.digital[13].write(1)
        else:
            board.digital[13].write(0)
        board.exit()
'''
# driver function

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)


