const startBtn = document.getElementById('start-record');
const stopBtn = document.getElementById('stop-record');
const statusText = document.getElementById('status');
const resultDiv = document.getElementById('result');

let recording = false;

startBtn.addEventListener('click', () => {
    statusText.textContent = '🎤 Listening...';
    recording = true;
    startBtn.disabled = true;
    stopBtn.disabled = false;
    resultDiv.style.display = 'none';
    
    // Simulate the start of recording
    setTimeout(() => {
        fetch('/analyze', { method: 'POST' })
            .then(response => response.text())
            .then(result => {
                resultDiv.innerHTML = `<div class="result-card">
                    <h3>🎯 Sentiment Analysis Result</h3>
                    <p>${result}</p>
                </div>`;
                resultDiv.style.display = 'block';
                statusText.textContent = '📊 Recording stopped and analyzed!';
            })
            .catch(error => {
                console.error('Error:', error);
                statusText.textContent = '❌ Error in processing audio.';
            });
    }, 3000);  // Simulate a delay to mimic recording time
});

stopBtn.addEventListener('click', () => {
    if (recording) {
        statusText.textContent = '⏳ Processing...';
        startBtn.disabled = false;
        stopBtn.disabled = true;
        recording = false;
    }
});
