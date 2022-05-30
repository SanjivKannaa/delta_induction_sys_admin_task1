function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
}

function home(){
    window.open("index.html", "_self");
}

function click(number) {
    document.getElementById("button1").click();
}

function start(){
    window.open("level1_run.html", "_self");
}


function level2(){
    window.open("level2.html", "_self");
}


window.onload = function () {
    start();
    sleep(5000);
};
