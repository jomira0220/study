// 서버 세팅 
let express = require("express");
let app = express();
let port = 3203;
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
    res.redirect("loginForm"); // res.redirect() 는 라우터이동.
});
app.get("/loginForm", function(req, res){ 
    res.render("loginForm.ejs"); 
});
app.get("/loginPro", function(req, res){ 
    
    let id = req.query.id; //지정한 변수명으로 가져옴
    let pw = req.query.pw;
    
    let dbId = 'qwer'
    let dbPw = '1234'
    
    
    let check = -1;
    if( id == dbId && pw == dbPw) {
        check = 1;
    }
    
    let result = {
        "check" : check
    }
    /*
    let url = require('url');
    let urlObject1 = url.parse('http://localhost:3203/loginPro?id=qwer&pw=1111').query;
    let urlObject2 = url.parse('http://localhost:3203/loginPro?id=qwer&pw=1111',true).query;
    console.log(urlObject1)
    console.log(urlObject2)
    console.log(url.parse().query.id)
    */
    
    res.render("loginPro.ejs",result); //결과값을 랜더뒤에 추가
});


