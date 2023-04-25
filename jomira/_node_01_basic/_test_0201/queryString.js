/* express를 통하여 ejs를 사용하지 않은 형태로 아래와
같이 작업도 가능 */

var http = require('http');
var url = require('url');

var app = http.createServer(function(request,response){
    var queryData = url.parse(request.url, true).query;
    var template = `
    <head></head>
    <body>
    <h2> ${queryData.id} </h2>
    <ul>
      <li><a href="/?id=LEE">LEE</a></li>
      <li><a href="/?id=PARK">PARK</a></li>
      <li><a href="/?id=JEONG">JEONG</a></li>
    </ul>
    <body>   
    `
	response.end(template);
});

app.listen(4000);