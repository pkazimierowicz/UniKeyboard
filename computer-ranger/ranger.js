const noble = require('noble');

let closest_beacon = null;

noble.on('stateChange', function(state) {
  if (state === 'poweredOn') {
    console.log('scanning...');
    noble.startScanning([], true);
  }
  else {
    noble.stopScanning();
  }
});

noble.on('discover', function(peripheral) {
    //noble.stopScanning();
    console.log('found peripheral:', peripheral.advertisement);
});

module.export = () => { return closest_beacon; };
