// 서버 세팅 
let express = require("express");
let app = express();
let port = 3202;
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// ejs 세팅(views)
let ejs = require("ejs");
app.set("views", __dirname + "/views");
app.set("view engine", "ejs");
app.engine("ejs", ejs.renderFile);


// 라우터 세팅
app.get("/", function(req, res){ 
    res.redirect("main"); // res.redirect() 는 라우터이동.
});

// res.render 하나당 ejs파일을 하나씩 추가한다. 
app.get("/main", function(req, res){ 
    res.render("main.ejs"); // res.render() 는 ejs 파일을 출력한다. 
});


// 라우터 폴더 세팅
// ./ 또는 __dirname => 현재 폴더를 의미
require("./router/game99")(app); 
require(__dirname + "/router/gameBR31")(app);