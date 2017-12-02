const server = require("./networking");
server((beaconid, address) => {
  console.log(`${address} has beacon id ${beaconid}`);
});
