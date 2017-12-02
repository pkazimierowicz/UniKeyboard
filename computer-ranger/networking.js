const dgram = require('dgram');
const server = dgram.createSocket('udp4');

const beacon_mappings = {};
module.exports = {
  server() {
    server.on('error', (err) => {
      console.error(`UDP server error:\n${err.stack}`);
      server.close();
      process.exit(0);
    });

    server.on('message', (msg, rinfo) => {
      beacon_mappings[msg] = rinfo.address;
    });

    server.on('listening', () => {
      const address = server.address();
      console.log(`UDP server listening ${address.address}:${address.port}`);
    });

    server.bind(41234);
  },
  sendto(beaconid, payload) {
    const message = new Buffer(payload);
    const client = dgram.createSocket('udp4');
    const PORT = 41235;
    const HOST = beacon_mappings[beaconid];

    if(!HOST) {
      console.warn("Unknown beacon: ", beaconid);
      return;
    }

    console.log(`Sending ${message} to ${HOST}:${PORT}`);
    client.send(message, 0, message.length, PORT, HOST, function(err, bytes) {
        if (err) throw err;
        client.close();
    });
  }
};
