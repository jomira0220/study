export class PageIndex {
    
    execute(){
        let $content = document.querySelector("#content");
        
        let tag = ""
        
        tag += 
        `
        <h1>이곳은 메인페이지입니다.</h1>
        `;
        
        $content.innerHTML = tag;
        
    }
    
}