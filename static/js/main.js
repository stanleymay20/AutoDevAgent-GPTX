function sendTask() {
    const input = document.getElementById("task-input").value;
    if (!input.trim()) return;
  
    document.getElementById("status").innerText = "Processing...";
    fetch("/dashboard/execute", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task: input })
    })
      .then(res => res.json())
      .then(data => {
        document.getElementById("status").innerText = "Complete";
        document.getElementById("agent-response").innerText = data.response;
      })
      .catch(err => {
        document.getElementById("status").innerText = "Error";
        console.error(err);
      });
  }
  
  function sendCommand() {
    const input = document.getElementById("console-input").value;
    if (!input.trim()) return;
  
    document.getElementById("console-output").innerText = "Executing...";
    fetch("/dashboard/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: input })
    })
      .then(res => res.json())
      .then(data => {
        document.getElementById("console-output").innerText = data.result;
      })
      .catch(err => {
        document.getElementById("console-output").innerText = "Execution error.";
        console.error(err);
      });
  }
  
  // Voice interaction
  let recorder;
  document.getElementById("start-recording").onclick = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);
    const chunks = [];
  
    recorder.ondataavailable = e => chunks.push(e.data);
    recorder.onstop = () => {
      const blob = new Blob(chunks, { type: "audio/webm" });
      const formData = new FormData();
      formData.append("audio", blob);
  
      fetch("/voice/whisper", { method: "POST", body: formData })
        .then(res => res.json())
        .then(data => {
          document.getElementById("transcript").innerText = data.transcript;
          document.getElementById("voice-response").innerText = data.response;
        });
    };
  
    recorder.start();
  };
  
  document.getElementById("stop-recording").onclick = () => recorder.stop();
  