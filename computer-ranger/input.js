"use strict";

const EvdevReader = require("evdev");

module.exports = (callback) => {
  const reader = new EvdevReader();

  reader.on("EV_KEY",function(data){
    let payload = {
      type: "EV_KEY",
      payload: data
    };
    callback(payload);
  }).on("EV_REL",function(data){
    let payload = {
      type: "EV_REL",
      payload: data
    };
    callback(payload);
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
