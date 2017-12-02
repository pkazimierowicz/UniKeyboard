const noble = require('noble');
const ourBeacons = [ "D0D3FA86CA7645EC9BD96AF43D4688EC", "D0D3FA86CA7645EC9BD96AF4BD825E79", "D0D3FA86CA7645EC9BD96AF4A17D1214", "D0D3FA86CA7645EC9BD96AF48B479BA7" ];

let closest_beacon = null;

noble.on('stateChange', function(state) {
  if (state === 'poweredOn') {
    console.log('scanning...');
    noble.startScanning(ourBeacons, true);
  }
  else {
    noble.stopScanning();
  }
});

noble.on('discover', function(peripheral) {
    //noble.stopScanning();
    console.log('found peripheral:', peripheral);
});

module.export = () => { return closest_beacon; };
