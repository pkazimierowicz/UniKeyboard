"use strict";

const noble = require('noble');
const includes = require('lodash.includes');
const ourBeacons = [ "D0D3FA86CA7645EC9BD96AF43D4688EC", "D0D3FA86CA7645EC9BD96AF4BD825E79", "D0D3FA86CA7645EC9BD96AF4A17D1214", "D0D3FA86CA7645EC9BD96AF48B479BA7" ];
const ourBeaconsUUIDs = ["d41f474e5a80", "c945e42f7c7a", "fc75731cb160", "ce019d3a8064"];
const ourBeaconsADDRs = ["d4:88:47:76:7f:80", "d4:88:47:76:7f:80", "c9:5a:42:e5:6e:7a", "ce:49:7c:fe:6d:64"];

let lastOurSignal = -256;
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
	if(peripheral.rssi > -30)
    console.log(peripheral.uuid, includes(ourBeaconsUUIDs, peripheral.uuid), peripheral.address);
  if (!includes(ourBeaconsADDRs,peripheral.address)) {return}
	else {
		if (peripheral.rssi > lastOurSignal){
			lastOurSignal = peripheral.rssi;
			closest_beacon = peripheral.address
			console.log("Chosen device: " + peripheral.address);
		}
	}
});

module.exports = () => { return closest_beacon; };
