import { ControllerMain } from "./controllerMain.js";

export class PageHeader {
    execute(){
        let $header = document.querySelector("#header");
        let tag = ""
        
        
        tag += 
        `
        <style>
        *{ margin:0; padding:0; }
        #header-top {
            width:800px;
            margin:0 auto;
            border: 1px solid #000;
        }
        h1,ul {
            display:inline-block;
        }
        ul li {
            display:inline-block;
        }
        </style>
        `;
        
        tag += 
        `
        <div id="header-top">
        <h1>로고</h1>
        <ul>
            <li><a href="">메뉴1</a></li>
            <li><a href="">메뉴2</a></li>
            <li><a href="">메뉴3</a></li>
        </ul>
        <button id="button-memberJoinPage">회원가입</button>
        <button id="button-memberLoginPage">로그인</button>
        </div>
        `;
        
        $header.innerHTML = tag;
        
        let $joinBtn = document.querySelector("#button-memberJoinPage")
        let $LoginBtn = document.querySelector("#button-memberLoginPage")
        
        $joinBtn.addEventListener("click",this.buttonMemberJoinPageClick)
        $LoginBtn.addEventListener("click",this.buttonMemberLoginPageClick)
        
        /*
        let buttonMemberJoinPageClick = $joinBtn.addEventListener("click",(event) => {
            console.log("1")
        })
        let buttonMemberLoginPageClick =  $LoginBtn.addEventListener("click",(event) => {
            console.log("2")
        })
        */
        
        
    }
    
    
    buttonMemberJoinPageClick = (event) => {
        // ControllerMain.getInstance().changePage("page-memberJoin");
    }
    
    buttonMemberLoginPageClick = (event) => {
        //ControllerMain에 있는 changePage함수를 활용하여 페이지 변경처리
        ControllerMain.getInstance().changePage("page-memberLogin");
        // console.log("2")
    }
    
}