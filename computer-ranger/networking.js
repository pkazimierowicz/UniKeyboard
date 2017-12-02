const dgram = require('dgram');
const server = dgram.createSocket('udp4');

module.exports = (callback) => {
  server.on('error', (err) => {
    console.error(`UDP server error:\n${err.stack}`);
    server.close();
    process.exit(0);
  });

  server.on('message', (msg, rinfo) => {
    callback(msg, rinfo.address)
  });

  server.on('listening', () => {
    const address = server.address();
    console.log(`UDP server listening ${address.address}:${address.port}`);
  });

  server.bind(41234);
};
