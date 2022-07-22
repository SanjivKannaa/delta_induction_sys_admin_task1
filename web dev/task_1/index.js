function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
}



function developer_information(){
  window.open("developer_information.html", "_self");
}

function leaderboard(){
  window.open("leaderboard.html", "_self");
}

document.body.requestFullscreen();
function startgame(){
    sleep(2000);
    window.open("single.html", "_self", "fullscreen=yes");
}