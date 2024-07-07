
alert("this is fun");

document.addEventListener("DOMContentLoaded", (Event) =>{
    const textArea = document.getElementById("textArea");

    textArea.addEventListener('input', (Event) =>{
        textArea.style.height = 'auto';
        textArea.style.height = textArea.scrollHeight + 'px';
    });

    textArea.addEventListener("keypress", (Event) =>{
        textArea.style.borderColor = "red";
    });

    textArea.style.height = textArea.scrollHeight + 'px';
});