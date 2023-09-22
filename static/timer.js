// quiz_timer.js

var countDownDate = sessionStorage.getItem('countDownDate');
if (!countDownDate) {
    countDownDate = new Date();
    countDownDate.setMinutes(countDownDate.getMinutes() + 1);
    sessionStorage.setItem('countDownDate', countDownDate);
} else {
    countDownDate = new Date(countDownDate);
}

var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;

    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s ";

    if (distance < 0) {
        clearInterval(x);
        document.getElementById("timer").innerHTML = "Time's Up!";
        nextQuestion(); // Automatically submit the form when time is up
    }
}, 1000);

function nextQuestion() {
    document.getElementById("quizForm").submit(); // Submit the form
}

function resetTimer() {
            countDownDate = new Date();
            countDownDate.setMinutes(countDownDate.getMinutes() + 1);
            sessionStorage.setItem('countDownDate', countDownDate);

            var now = new Date().getTime();
            var distance = countDownDate - now;

            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s ";
}

document.getElementById('startRoundBtn').addEventListener('click', resetTimer);
