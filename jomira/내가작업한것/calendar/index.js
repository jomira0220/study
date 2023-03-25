


//!현재 타임 노출
function setTime(calendarBox) {
  calendarBox.querySelector(".nowTime").innerText = new Date().toLocaleTimeString();
}

//!현재 년,월,일,요일 노출
function setDate(calendarBox) {
  let thisYear = new Date().getFullYear();
  let thisMonth = new Date().getMonth();
  let thisDate = new Date().getDate();
  let thisDay = new Date().getDay();
  let dayList = ["일", "월", "화", "수", "목", "금", "토"];
  calendarBox.querySelector(".nowDate").innerText = thisYear+`년 `+ (thisMonth + 1) + `월 ` + thisDate +`일 `+ dayList[thisDay] +`요일`;
  calendarBox.querySelector("#year input").value = thisYear
  calendarBox.querySelector("#month input").value = thisMonth + 1
}


function dayTableSet(calendarBox){

  let dayList = ["일", "월", "화", "수", "목", "금", "토"];
  let $columnHeaderWarp = document.createElement("div")
  $columnHeaderWarp.id = "columnHeaderWarp"
  daySection.append($columnHeaderWarp)
  
  dayList.forEach((el) => {
    let $columnHeader = document.createElement("div");
    $columnHeader.setAttribute("role","columnHeader"); 
    $columnHeaderWarp.append($columnHeader)

    $columnHeader.innerText = el
  })
  
  for(let i = 0; i < 35; i++){
    let $dayBox = document.createElement("div");
    $dayBox.classList = "day"
    $dayBox.innerHTML = `<div class="dayNum"></div>`
    daySection.append($dayBox)
  }
  
}

function dayDataSet(calendarBox){
  let yearCheck = calendarBox.querySelector("#year input").value
  let monthCheck = calendarBox.querySelector("#month input").value - 1 //
  
  //구하려는 년도와 월의 1일 요일(인덱스) & 말일(일자)
  let nowYear = new Date().getFullYear()
  let nowMonth = new Date().getMonth()
  let nowDate = new Date().getDate()

  let firstIndex = new Date(yearCheck, monthCheck, 1).getDay()
  let lastDate = new Date(yearCheck, monthCheck+1, 0).getDate()
  
  let daySection = calendarBox.querySelector("#daySection")
  let dayNumBox = daySection.querySelectorAll(".dayNum")
  let dayBox = daySection.querySelectorAll(".day")
  
  
  let dayFirst = 1
  for(let i = 0; i < 7*5; i++){
  
    if(i >= firstIndex && dayFirst <= lastDate){
      dayBox[i].classList.remove("noday")
      dayNumBox[i].innerText = dayFirst
      if(dayFirst == nowDate && monthCheck == nowMonth && nowYear == yearCheck){
        dayBox[i].classList.add("toDay")
      }else{
        dayBox[i].classList.remove("toDay")
      }
      dayFirst++
    }else{
      dayBox[i].classList.add("noday")
      dayNumBox[i].innerText = ""
    }
    
  }

}


function changeEvent(calendarBox){
  let controlBox = calendarBox.querySelector("#controlBox")
  let plusBtn = controlBox.querySelector(".plusBtn");
  let minusBtn = controlBox.querySelector(".minusBtn");
  
  let monthInput = controlBox.querySelector("#month input");
  let month = Number(monthInput.value);
  
  let yearInput = controlBox.querySelector("#year input");
  let year = Number(yearInput.value);
  
  monthInput.addEventListener("change", (event) => {
    month = Number(monthInput.value)
    dayDataSet(calendarBox)
  });
  yearInput.addEventListener("change", (event) => {
    year = Number(yearInput.value)
    dayDataSet(calendarBox)
  });
  
  
  plusBtn.addEventListener("click", () => {
    if(1 <= month && month < 12){
      month += 1
    }
    monthInput.value = month
    dayDataSet(calendarBox)
  });
  
  minusBtn.addEventListener("click", () => {
    if(1 < month && month <= 12){
      month -= 1
    }
    monthInput.value = month
    dayDataSet(calendarBox)
  });
  
  
}



//!캘린더 기본 구조 셋팅 및 함수호출
function calendar(elId){
  
  let date = new Date();
  let calendarBox = document.querySelector(elId)
  
  if(calendarBox){
      calendarBox.innerHTML = `
        <div id="header">
          <h1><div><img src="calendar.png" alt="Calendar"></div></h1>
          <div id="controlBox">
              <div id="yearControl">
                <div id="year"><input type="number" value="" min="1"><span>년</span></div>
              </div>
              <div id="monthControl">
                <button class="minusBtn" type="button"><i class="fas fa-angle-down"></i></button>
                <span id="month"><input type="number" value="" min="1" max="12">월</span>
                <button class="plusBtn" type="button"><i class="fas fa-angle-up"></i></button>
              </div>
          </div>
          <div id="nowWarp">
            <div class="nowDate"></div>
            <div class="nowTime"></div>
          </div>
        </div>
        <div id="daySection"></div>
      `;
  }
  setInterval(() => {setTime(calendarBox)}, 1000);
  setDate(calendarBox);
  dayTableSet(calendarBox);
  dayDataSet(calendarBox)
  changeEvent(calendarBox)
}

calendar("#calendarBox")


