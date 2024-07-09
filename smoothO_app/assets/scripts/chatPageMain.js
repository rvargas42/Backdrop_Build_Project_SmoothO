

document.getElementById('textArea').addEventListener('input', function () {
    this.style.height = 0;
    const parent = document.getElementById("rightPanel");
    const parent_height = parent.getBoundingClientRect().height;
    const scrollHeight = this.scrollHeight;

    if (scrollHeight < 0.30 * parent_height) {
        this.style.height = scrollHeight + 'px';
    } else {
        this.style.height = 0.30 * parent_height + 'px';
    }
}, false);