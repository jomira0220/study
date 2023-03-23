let size = 3;
let $body = document.body;
let $table = document.createElement("table")
let $tdList = [];
let dataList = []; // player1(1), player2(2)
let turn = true; // player1(true), player2(false)
let win = 0; // player1(1), player2(2)

function init(){
  
  for(let i = 0; i < size; i++){
    let temp = [];
    for(let j = 0; j < size; j++){
      temp.push(0)
    }
    dataList.push(temp)
  }
  console.log(dataList)
  

  
  $body.append($table)
  for(let i = 0; i < size; i++){
    
    let $temp = []
    let $tr = document.createElement("tr")
    $table.append($tr)
    
    for(let j = 0; j < size; j++){
      
      let $td = document.createElement("td") 
      $tr.append($td)
    
      $td.addEventListener("click",clickEvent)
      $temp.push($td)
    
    }
    
    $tdList.push($temp)
    
  }
  
  console.log($tdList)
}

function clickEvent(){
  for(let i = 0; i < size; i++){
    for(let j = 0; j < size; j++){
      if(this == $tdList[i][j]){

        if(this.innerText == ""){
          if(turn){
            this.innerText = "O"
            dataList[i][j] = 1
          }else{
            this.innerText = "X"
            dataList[i][j] = 2
          }
          turn = !turn
        }
        
      }
    }
  }
  
  winCheck()
}


function winCheck(){
  //가로검사
  for(let i = 0; i < size; i++){
    if(dataList[i][0] == 1 && dataList[i][1] == 1 && dataList[i][2] == 1){
      win = 1
    }
    if(dataList[i][0] == 2 && dataList[i][1] == 2 && dataList[i][2] == 2){
      win = 2
    }
  }
  console.log(win)
  
  //세로검사
  
  //대각선/검사
  
  //대각선\검사
  
  //무승부
}


init()



/* ===================================================== */