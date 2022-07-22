var keys = Object.keys(localStorage);
var scores = [];
for(i of keys){
    scores.push([ parseInt(localStorage.getItem(i)),i]);
}

function sortFunction(a, b) {
    if (a[0] === b[0]) {
        return 0;
    }
    else {
        return (a[0] < b[0]) ? -1 : 1;
    }
}

scores.sort(sortFunction);
scores.reverse();
for(i of scores){
    var li = document.createElement('li');
var text  =document.createTextNode(i[1]  + "  -  " + String(i[0]));

li.appendChild(text);
document.getElementById('list').appendChild(li);

}


console.log(scores);



function home(){
    window.open("index.html", "_self");
}