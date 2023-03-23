
function calendar(elId){
    let calendarBox = document.querySelector(elId)
    if(calendarBox){
        calendarBox.innerHTML = `
          <div></div>
          <div></div>
        `;
    }
}

calendar("#calendarBox")