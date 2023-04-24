// 서버 세팅 
let express = require("express"); // express 변수생성
let app = express();              // app 에 express변수 저장
let port = 3101;				  // 포트번호 생성 
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});
