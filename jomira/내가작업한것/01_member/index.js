import { JsonMember } from "./jsonMember.js";
import { ControllerMain } from "./controllerMain.js";

// 여기가 시작지점이다. 
// Controller 클래스는 싱글톤
ControllerMain.getInstance().start();
JsonMember.getInstance().start();