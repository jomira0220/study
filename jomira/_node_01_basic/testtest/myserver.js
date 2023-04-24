//express 세팅
let express = require("express");
let app = express();
let port = 80;
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// ejs 세팅(views)
var ejs = require("ejs");
app.set("views", __dirname + "/views"); //__dirname 현재폴더
app.set("view engine", "ejs");
app.engine("ejs", ejs.renderFile);


// 라우터 세팅
app.get("/", function(req, res){ 
    res.render("test001.ejs"); 
});

app.get("/", function(req, res){ 
    res.render("test002.ejs"); // res.render() 는 ejs 파일을 출력한다. 
});