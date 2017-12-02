"use strict";

const networking = require("./networking");
const input = require("./input");
const ranger = require("./ranger");

networking.server()
input((payload) => {
  networking.sendto(ranger(), JSON.stringify(payload));
});
