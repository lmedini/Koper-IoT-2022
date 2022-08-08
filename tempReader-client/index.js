const { SerialPort } = require('serialport')
const { ReadlineParser } = require('@serialport/parser-readline')
const axios = require('axios').default

// TODO: configure the port name here
const portName = 'COM11'

// Create a port
const port = new SerialPort({
  path: portName,
  baudRate: 9600,
})

// Get the temperature value
// https://serialport.io/docs/api-parsers-overview
const parser = new ReadlineParser()
port.pipe(parser)

parser.on('data', (data) => {
	const url = "http://10.201.60.55:5000/temp/" + 100*data
	axios({
	  method: 'put',
	    url: url
	});
	console.log(data + " sent...")
})


//parser.on('data', console.log)
