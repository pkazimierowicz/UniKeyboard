const networking = require("./networking");
networking.server();

setInterval(() => {
  networking.sendto("asd", "HEJ!");
}, 1000);
