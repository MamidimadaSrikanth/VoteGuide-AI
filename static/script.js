//Voice Input Function
function startVoice() {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Voice not supported in this browser");
        return;
    }

    let recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";

    recognition.onresult = function (event) {
        let text = event.results[0][0].transcript;
        document.getElementById("userInput").value = text;
        sendMessage(); // auto send
    };

    recognition.start();
}

//Chat Function
async function sendMessage() {
    let input = document.getElementById("userInput").value;

    let res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    });

    let data = await res.json();

    document.getElementById("messages").innerHTML +=
        "<p><b>You:</b> " + input + "</p>" +
        "<p><b>Bot:</b> " + data.response + "</p>";
}

//Eligibility
async function checkEligibility() {
    let age = document.getElementById("age").value;
    let citizen = document.getElementById("citizen").value;

    let res = await fetch("/eligibility", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ age: age, citizen: citizen })
    });

    let data = await res.json();
    alert(data.result);
}

//Timeline
async function getTimeline() {
    let res = await fetch("/timeline");
    let data = await res.json();

    let output = "";
    for (let key in data) {
        output += "<p>" + key + ": " + data[key] + "</p>";
    }
    document.getElementById("timeline").innerHTML = output;
}