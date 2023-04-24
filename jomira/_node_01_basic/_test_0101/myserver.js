let express = require("express");
let app = express();
let port = 3101;
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// ejs 세팅(views)
let ejs = require("ejs");           // ejs 변수생성
app.set("views", __dirname);        // 경로설정 
app.set("view engine", "ejs");      // ejs세팅1  
app.engine("ejs", ejs.renderFile);  // ejs세팅2  
