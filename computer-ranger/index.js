var noble = require('noble');


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
    noble.stopScanning();
    console.log('found peripheral:', peripheral.advertisement);
});