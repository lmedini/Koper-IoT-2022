const { SerialPort } = require('serialport')

// Create a port
const port = new SerialPort({
  path: 'COM9',
  baudRate: 9600,
})

// Switches the port into "flowing mode"
port.on('data', function (data) {
  console.log('Data:', data)
})
