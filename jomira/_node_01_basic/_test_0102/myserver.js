// 서버 세팅 
let express = require("express");
let app = express();
let port = 3102;
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// ejs 세팅(views)
let ejs = require("ejs");           // ejs 변수생성
app.set("views", __dirname);        // 경로설정 
app.set("view engine", "ejs");      // ejs세팅1  
app.engine("ejs", ejs.renderFile);  // ejs세팅2  


// 라우터 세팅 - 파일이 직접 노출되지 않도록 해줌
// res.render 하나당 ejs파일을 하나씩 추가한다. 
app.get("/ex01", function(req, res){ 
    res.render("ex01.ejs"); 
});