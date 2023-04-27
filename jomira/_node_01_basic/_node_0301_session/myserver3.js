// 서버 세팅 
let express = require("express");
let app = express();
let port = 3301;
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// ejs 세팅(views)
let ejs = require("ejs");
app.set("views", __dirname + "/views");
app.set("view engine", "ejs");
app.engine("ejs", ejs.renderFile);


// session 세팅
let session = require("express-session");
app.use(session({
	secret : "abcdefg",
	resave : false, 
	saveUninitialized : false 
}));


// 라우터 세팅
app.get("/", function(req, res){ 
    // session 디비 세팅 (난중에 database 로 변경된다.)
    let gameDB = []; 
    let count = 0;
    while (true){
        let r = Math.floor(Math.random() * 90 + 10);
        let check = false;
        for (let j = 0; j < gameDB.length ; j++){
            if (gameDB[j] == r){
                check = true;
                break;
            }
        }
        if (check == false){
            gameDB.push(r);
            count += 1;
            if (count == 25){
                break
            }
        }
    }
    let max = 0;
    for (let i = 0; i < 25; i++){
        if (max < gameDB[i]){
            max = gameDB[i];
        }
    }
    console.log(gameDB);
    console.log(max);
    req.session.max = max;
    req.session.gameDB = gameDB; 
    req.session.gameover = false; 
    req.session.hint = false;
    res.redirect("maxGame"); 
});


app.get("/maxGame", function(req, res){  

    let renderData = {
        "gameDB" : req.session.gameDB,  
        "max" : req.session.max,
        "gameover" : req.session.gameover,
        "hint" : req.session.hint
    };
    res.render("_0301_maxGame.ejs", renderData);
});

app.get("/maxGamePro", function(req, res){  

    let index = req.query.index;
    let max = req.session.max;
    let gameDB = req.session.gameDB;
    let gameover = req.session.gameover;
    let hint = req.session.hint;
    console.log(max);
    console.log(hint);

    if (gameDB[index] == max){
        gameDB[index] = 0;
        hint = false;
    }

    max = 0;
    for (let i = 0; i < 25; i++){
        if (max < gameDB[i]){
            max = gameDB[i];
        }
    }


    let count = 0;
    for(let i = 0; i < gameDB.length; i++){
        if(gameDB[i] == 0){
            count += 1;
        }
    }
    if (count == 25) {
        gameover = true;
    }

    req.session.max = max;
    req.session.gameDB = gameDB; 
    req.session.gameover = gameover; 
    req.session.hint = hint;

    res.redirect("maxGame");
});


app.get("/hintPro", function(req, res){  

    req.session.hint = true;    

    res.redirect("maxGame");
});


