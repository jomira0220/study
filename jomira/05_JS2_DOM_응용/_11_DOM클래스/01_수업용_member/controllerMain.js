//각 페이지들의 총 모음 실행

import { PageHeader } from "./pageHeader.js";
import { PageIndex } from "./pageIndex.js";
import { PageMemberLogin } from "./pageMemberLogin.js";

export class ControllerMain {
    
    static instance = new ControllerMain()
    static getInstance() { return this.instance; }
    
    start(){
        this.pageList = {};
        this.setPageList();
        
        this.changePage("page-index")
        this.changePage("page-header")
        //this.changePage("page-memberLogin")
    }
    
    setPageList(){
        this.pageList["page-header"] = new PageHeader();
        this.pageList["page-index"] = new PageIndex();
        this.pageList["page-memberLogin"] = new PageMemberLogin();
    }
    
    changePage(pageName){
        this.pageList[pageName].execute()
    }
    
}