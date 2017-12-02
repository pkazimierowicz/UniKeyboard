"use strict";

const EvdevReader = require("evdev");
const groupby = require("lodash.groupby");

module.exports = (callback) => {
  let ev_rel = [];

  setInterval(() => {
    let groups = groupby(ev_rel, (v) => v["code"]);
    ev_rel = [];
    let reduced = Object.values(groups).map((g) => g.reduce((acc, v) => {
      if(!acc) return v;
      acc.value += v.value;
      return acc;
    }, null));
    reduced.forEach((data) => {
      let payload = {
        type: "EV_REL",
        payload: data
      };
      callback(payload);
    });
  }, 15);

  const reader = new EvdevReader();

  reader.on("EV_KEY",function(data){
    let payload = {
      type: "EV_KEY",
      payload: data
    };
    callback(payload);
  }).on("EV_REL",function(data){
    ev_rel.push(data);
  }).on("error",function(e){
    console.log("reader error : ",e);
  })

  reader.search("/dev/input/by-path","kbd",function(err,files){
    if(err){
      console.log("node-evdev search stream : ", err);
    }else if(files[0]){
      console.log("found %s inputs",files.length);
      var device = reader.open(files[0]);
      device.on("open",function(){
        console.log(device.id);
      })
    }
  });

  reader.search("/dev/input/by-path","mouse",function(err,files){
    if(err){
      console.log("node-evdev search stream : ", err);
    }else if(files[0]){
      console.log("found %s inputs",files.length);
      var device = reader.open(files[0]);
      device.on("open",function(){
        console.log(device.id);
      })
    }
  });
};
