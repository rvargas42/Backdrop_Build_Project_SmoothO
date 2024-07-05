document.addEventListener("DOMContentLoaded", function(){
    const textarea = document.getElementById("chatBar");
    textarea.addEventListener('input', function(){
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
    textarea.dispatchEvent(new Event('input'));
});