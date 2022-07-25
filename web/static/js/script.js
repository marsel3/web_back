
setInterval(function(){
    var r1 = document.getElementById('r1');
    var r2 = document.getElementById('r2');
    var r3 = document.getElementById('r3');
    var r4 = document.getElementById('r4');

    if (r1.checked) {document.getElementById("r1").checked = false;
        document.getElementById("r2").checked = true;}

    else if (r2.checked) {document.getElementById("r2").checked = false;
        document.getElementById("r3").checked = true;}
    
    else if (r3.checked) {document.getElementById("r3").checked = false;
        document.getElementById("r4").checked = true;}

    else if (r4.checked) {document.getElementById("r4").checked = false;
        document.getElementById("r1").checked = true;}

}, 5000);









