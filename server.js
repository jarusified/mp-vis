var http = require("http");
var fs = require("fs");
var port = process.env.PORT || 8000;
var url = require("url");
var path = require("path");

var mimeTypes = {
    "html": "text/html",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "js": "text/javascript",
    "css": "text/css"
};


var server = http.createServer(function(req,res){
    var uri = url.parse(req.url).pathname;
    var filename = path.join(process.cwd(), uri);
    fs.exists(filename, function(exist){
	if(!exist){
	    console.log("[404]" + filename);
	    res.writeHead(200, {'Content-Type': 'text/plain'});
	    res.write("404 Not found\n");
	    res.end();
	}
	var mimeType = mimeTypes[path.extname(filename).split(".")[1]];
	res.writeHead(200, {'Content-Type': mimeType });
	var fileStream = fs.createReadStream(filename);
	fileStream.pipe(res);
    });
}).listen(port);

var io = require("socket.io").listen(server, {log: true});
