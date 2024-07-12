// Función para alternar el tema
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    const lightbulb = document.querySelector("#light i");
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);

    if (newTheme === 'dark') {
        lightbulb.classList.remove("bi-moon-fill")
        lightbulb.classList.add("bi-brightness-high-fill");
    } 
    if (newTheme === 'light') {
        lightbulb.classList.remove("bi-brightness-high-fill")
        lightbulb.classList.add("bi-moon-fill");
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    toggleTheme();
});

// Agregar evento de clic al botón
document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("light");
    button.addEventListener("click", toggleTheme);
});