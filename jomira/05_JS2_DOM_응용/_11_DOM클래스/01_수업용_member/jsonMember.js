export class JsonMember {
    //Json은 아래처럼 싱글톤 패턴으로 작업한다!
    static instance = new JsonMember()
    static getInstance(){ return this.instance }
    
    //기본 초기값 셋팅
    start(){
        this.memberList = null;
        this.setSampleData();
    }
    
    setSampleData(){
        this.memberList = [
            {
                "memberId":"qwer1234",
                "memberPw":"Qwer1234!",
            },
            {
                "memberId":"apple1234",
                "memberPw":"Apple1234!",
            },
            {
                "memberId":"banana1234",
                "memberPw":"Banana1234!",
            },
        ]
    }
    
    //id와 비번을 전달받아서 위에 데이터와 비교
    memberLogin(memberId,memberPw){
        let check = false;
        for(let i = 0; i < this.memberList.length; i++){
            console.log(this.memberList[i].memberId)
            if(this.memberList[i].memberId == memberId && this.memberList[i].memberPw == memberPw){
                check = true
                return check
                break
            }
        }   
    }
    
}