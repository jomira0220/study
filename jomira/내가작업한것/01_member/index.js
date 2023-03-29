import { JsonMember } from "./jsonMember.js";
import { ControllerMain } from "./controllerMain.js";
import { JsonBoard } from "./jsonBoard.js";

// 여기가 시작지점이다. 
// Controller 클래스는 싱글톤
ControllerMain.getInstance().start();
JsonMember.getInstance().start();
JsonBoard.getInstance().start();

/*
//!헤더 상단 고정
let sticky = () => {
    document.addEventListener("scroll", function () {
        console.log("d")
      
      console.log(el.offsetTop);
      if (document.pageYOffset > el.offsetTop + 200) {
        el.classList.add("fixed");
      } else {
        el.classList.remove("fixed");
      }
      
    });
};
*/

function sticky() {
    document.addEventListener("scroll", function () {
        console.log("d")
    })
}

sticky()