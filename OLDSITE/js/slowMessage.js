var i = 0;
var message = "Molly.im";

function slowTitle() {
    if (i < message.length) {
        document.getElementById("title").innerHTML += message.charAt(i);
        i++;
        setTimeout(slowTitle, 110);
    }
}

slowTitle();
