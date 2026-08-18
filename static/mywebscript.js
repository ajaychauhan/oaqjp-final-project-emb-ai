let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            // Access status_code to correctly handle server responses
            if (this.status == 200) {
                let data = JSON.parse(this.responseText);
                let result = `For the given statement, the system response is 'anger': ${data.anger}, 'disgust': ${data.disgust}, 'fear': ${data.fear}, 'joy': ${data.joy} and 'sadness': ${data.sadness}. The dominant emotion is **${data.dominant_emotion}**.`;
                document.getElementById("system_response").innerHTML = result;
            } 
            else if (this.status == 400) {
                // Updated to display the exact required message
                document.getElementById("system_response").innerHTML = "<p>**Invalid text! Please try again!**</p>";
            } 
            else {
                document.getElementById("system_response").innerHTML = `Error: ${this.statusText}`;
            }
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}