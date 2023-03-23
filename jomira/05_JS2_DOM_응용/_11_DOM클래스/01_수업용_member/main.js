//실행을 담당할 페이지 - 시작페이지

import { ControllerMain } from "./controllerMain.js"
import { JsonMember } from "./jsonMember.js"

ControllerMain.getInstance().start()
JsonMember.getInstance().start()