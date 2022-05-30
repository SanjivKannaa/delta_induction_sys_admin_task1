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


document.body.requestFullscreen();
function startgame(){
    sleep(2000);
    window.open("level1.html", "_self", "fullscreen=yes");
}
highscore_value = 0;
document.body.innerHTML = "<p3 class='highscore' style='text-align: right'>Highscore => " + highscore_value + "</p3>";