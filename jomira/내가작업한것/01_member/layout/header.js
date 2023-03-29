import { ControllerMain } from "../controllerMain.js";

export class LayoutHeader {
  execute(data) {
    

    
    let $header = document.querySelector("#header");
    let tag = "";

    // [로그아웃] 상태 화면
    if (ControllerMain.getInstance().log == null) {
      tag += `
      <h1 id="btn-indexPage">logo</h1>
      <!--
      <ul class="gnb">
          <li id="btn-boardListPage">게시판</li></li>
          <li id="btn-boardListPaging">게시판 페이징</li>
          <li id="btn-memberListPage">회원 전체 목록</li>
      </ul>
      -->
      <ul class="userMenu">
        <li id="btn-memberJoinPage">회원가입</li>
        <li id="btn-memberLoginPage">로그인</li>
      </ul>
      `;
    } else {
      // [로그인] 상태 화면
      tag += `
      <h1 id="btn-indexPage">logo</h1>
      <ul class="gnb">
          <li id="btn-boardListPage">게시판</li></li>
          <li id="btn-boardListPaging">게시판 페이징</li>
          <li id="btn-memberListPage">회원 전체 목록</li>
      </ul>
      <ul class="userMenu">
        <li id="btn-memberLogoutPro">로그아웃</li>
      </ul>
      `;
    }
  

    
    $header.innerHTML = tag;

    let $indexPageBtn = document.querySelector("#btn-indexPage");
    let $joinPageBtn = document.querySelector("#btn-memberJoinPage");
    let $loginPageBtn = document.querySelector("#btn-memberLoginPage");
    let $boardPageBtn = document.querySelector("#btn-boardListPage");
    let $memberLogoutPro = document.querySelector("#btn-memberLogoutPro");

   // [로그아웃] 상태 화면
   if(ControllerMain.getInstance().log == null) {
    
      $indexPageBtn.addEventListener("click",() => { this.pageMove("page_content") }) 
      $loginPageBtn.addEventListener("click",() => { this.pageMove("page_memberLogin") })  
      $joinPageBtn.addEventListener("click",() => { this.pageMove("page_memberJoin") }) 
      
    }else{ 
    // [로그인] 상태 화면
      $boardPageBtn.addEventListener("click",() => { this.pageMove("page_boardList") }) 
      
      $memberLogoutPro.addEventListener("click",() => {  
        alert("로그아웃 되었습니다.");
        ControllerMain.getInstance().log = null;
        this.pageMove("layout_header")
        this.pageMove("layout_content")
      }) 
      
    }
  }// close execute
  
  
  
  //!페이지 이동 처리용
  pageMove = (pageName) => {
    ControllerMain.getInstance().changePage(pageName, null);
  }
  
  
}
