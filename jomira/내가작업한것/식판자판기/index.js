
const $button = document.querySelectorAll("button")

const $cashBtnMinus = document.querySelectorAll(".minusBtn")
const $cashBtnPlus = document.querySelectorAll(".plusBtn")

const $inventoryQuantity = document.querySelector("#inventoryQuantity")
const $adminCashList = document.querySelector("#adminCashList")

const $ticketPrice = document.querySelector("#ticketPrice").innerText.replace(/[^0-9]/g,"")


const $userCashChargingBtn = document.querySelector("#userCashChargingBtn")
const $userTicketBuyBtn = document.querySelector("#userTicketBuyBtn")

const buttonHover = () => {
  $button.forEach((e)=>{
    e.addEventListener("mouseover",() => {
      e.classList.add("on")
    })
    e.addEventListener("mouseout",() => {
      e.classList.remove("on")
    })
  })
}
buttonHover()


const cashBtnClick = () => {
  $cashBtnMinus.forEach((el,index)=>{
    el.addEventListener("click",() => {
      let countTd = el.parentElement.nextElementSibling.innerText
      let tempNum = Number(countTd)
      if(tempNum >= 1){
        tempNum--
        el.parentElement.nextElementSibling.innerText = tempNum
      }else{
        alert("1개이상 구매가능합니다.")
      }
      calCulation(el)
    })
  })
  
  $cashBtnPlus.forEach((el,index)=>{
    el.addEventListener("click",() => {
      let countTd = el.parentElement.previousElementSibling.innerText
      let tempNum = Number(countTd)
      tempNum++
      el.parentElement.previousElementSibling.innerText = tempNum
      calCulation(el)
    })
  })
}

cashBtnClick()


const calCulation = (el) => {
  let amountType = [50000,10000,5000,1000,500,100]
  
  let cashCountList = [];
  let cashTotalList = [];
  let cashTotal = 0;
  
  //계산할 요소의 부모테이블 선택
  let parentCashTable = el.closest("table");
  //console.log(parentCashTable)
  

  //부모의 안에 .cashTotal이 있는 경우와 없는 경우
  //잔돈충전하기 & 금액투입하기
  let cashTotalBox = parentCashTable.querySelector(".cashTotal")
  if(cashTotalBox){
    
    amountType.forEach(() => {
      cashCountList.push(0)
      cashTotalList.push(0)
    })
    
    parentCashTable.querySelectorAll(".count").forEach((el,index) => {
      cashCountList[index] = Number(el.innerText)
      cashTotalList[index] = Number(el.innerText) * amountType[index]
    })
    cashTotalList.forEach((el,index)=>{
      cashTotal += el
    })
    
    cashTotalBox.innerText = cashTotal.toLocaleString("ko-KR") + "원"
    
    function charging(){
        
        if(parentCashTable.closest("#adminTable") != null){
            let cashChargingBtn = parentCashTable.querySelector("#cashChargingBtn")
            cashChargingBtn.addEventListener("click",() => {
              $adminCashList.querySelectorAll("ul li span:not(.title)").forEach((el, index) => {
                  el.innerText = cashTotalList[index].toLocaleString("ko-KR") + `원`;
              });
            })
        }else{
          
        }
      
    }
    charging()
    
  }else{
     
    //식권충전하기 & 식권구입하기
    
     //충전할 식권개수 & 구매할 식권개수
    let ticketChargingBtn = parentCashTable.querySelector("#ticketChargingBtn"); //관리자 식권 충전 버튼
  
  
    if (ticketChargingBtn) {
      
      ticketChargingBtn.addEventListener("click", () => {
        let chargingTicketCount = parentCashTable.querySelector(".ticketCount").innerText.replace(/[^0-9]/g, ""); //충전할 식권 개수
        if (chargingTicketCount > 0) {
          $inventoryQuantity.innerHTML = chargingTicketCount + `개`;
          
          //사용자 금액투입하기 버튼 활성화
          $userCashChargingBtn.disabled = false;

          //사용자 금액투입하기 버튼 클릭시
          $userCashChargingBtn.addEventListener("click", () => {
            $userTicketBuyBtn.disabled = false;
          });
        }
      });
    }else{
      
      
      $userTicketBuyBtn.addEventListener("click",() => {
        let buyTicketCount = parentCashTable.querySelector(".ticketCount").innerText.replace(/[^0-9]/g, ""); //구매할 식권 개수
        let inventoryQuantityCount = Number($inventoryQuantity.innerText.replace(/[^0-9]/g, "")) //식권 재고 개수
        let userCashTotal = document.querySelector("#userCashTotal").innerText.replace(/[^0-9]/g,""); //사용자가 투입한 총금액
        let userBuyTotal = 0; //결제할 총 금액
        let userChange = 0; //거스름돈
        /*
          관리자에서 충전하는 금액이 상단에 누적되도록 처리필요 현재는 충전버튼 두번째 누르면 리셋하여 누적없이 새롭게 셋팅하는 형태로 되어있음
        
          유저가 구매후 남은 식권의 개수
          
          관리자돈으로 거스름 돈을 줄수 있는지 확인하여 
          부족시 관리자가 충전이 필요한 금액 안내
          부족하지 않아서 거슬러 줬다면 거슬러 주고 남은 금액 확인
          
          영수증 박스에다가 거스름돈 금액대별로 얼마인지랑 결제금액 투입금액 총거스름돈 출력시키기 -  해당이벤트는 영수증 출력하시겠습니까에 동의시 출력
          
        */
      
        //구매할 식권의 개수가 재고수량보다 많으면
        console.log(buyTicketCount + " " + inventoryQuantityCount)
        
        if(buyTicketCount > inventoryQuantityCount){
          alert("구매가능한 식권의 개수는" + inventoryQuantityCount + "개입니다.")
        }else{
          //구매할 식권의 개수가 재고수량과 같거나 적으면
        
          //유저가 결제할 총금액
          userBuyTotal = $ticketPrice * buyTicketCount
          
          //유저가 낸 금액보다 결제할 금액이 더 크면
          if(userCashTotal < userBuyTotal){
            let shortfallAmount = userBuyTotal - userCashTotal
            alert(shortfallAmount.toLocaleString("ko-KR") + "원이 모자랍니다.")
          }else{
            //유저가 낸 금액보다 결제할 금액이 작거나 같으면
            userChange = userCashTotal - userBuyTotal
            console.log("거스름돈 = " + userChange)
            
            let result = confirm("구매가 완료되었습니다. 영수증을 받으시겠습니까?")
            if(result){
              document.querySelector("#receipt").style.display = "flex"
              //alert("영수증 발행")
            }else{
              alert("영수증 미발행")
            }
          }
          
          
        }
      })
    }
    
    
    
  
  }
  
 
  
  //console.log(cashCountList)
  //console.log(cashTotalList)
  //console.log(cashTotal)
  
}





function ticketBox(boxId){
  let $ticketMachine = document.querySelector(boxId)
  $ticketMachine.innerHTML = `
  
  `
}
//ticketBox("#ticketMachine")