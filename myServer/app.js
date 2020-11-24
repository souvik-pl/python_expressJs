const express = require('express');
const http = require('http');
const path = require('path');

const app = express();

var server = http.createServer(app);


app.get('/image', function(req,res){
  res.sendFile(path.join(__dirname,'./public/image.jpg'));
});




server.listen(3000, function(){
  console.log("server is listening on port: 3000");
});
