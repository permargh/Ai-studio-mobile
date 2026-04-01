function processInput() {
    const input = document.getElementById('userInput').value;
    const output = document.getElementById('output');
    
    if (input.trim() === '') return;
    
    const userMsg = document.createElement('p');
    userMsg.innerHTML = `<strong style="color: #667eea;">You:</strong> ${input}`;
    output.appendChild(userMsg);
    
    const aiMsg = document.createElement('p');
    aiMsg.innerHTML = `<strong style="color: #764ba2;">AI:</strong> Processing your message...`;
    output.appendChild(aiMsg);
    
    document.getElementById('userInput').value = '';
}
