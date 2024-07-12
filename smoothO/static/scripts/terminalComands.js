document.addEventListener('DOMContentLoaded', function() {
    const terminalBody = document.getElementById('terminal');
    let isLastPromptFilled = false;

    // Función para limpiar todos los inputs
    function clearAllInputs() {
        terminalBody.innerHTML = '';
        focusLastTextarea();
    }

    // Manejar clic en la terminal para activar el cursor en el último input
    terminalBody.addEventListener('click', function(event) {
        if (event.target.classList.contains('terminal-input')) {
            focusLastTextarea(); // Enfocar la última textarea al hacer clic en la terminal
        }
    });

    terminalBody.addEventListener('keydown', function(event) {
        const terminalInput = event.target;

        if (event.key === 'Enter') {
            const command = terminalInput.value.trim();
            
            if (command.toLowerCase() === "clear")
                clearAllInputs();
            else
            {
                if (command)
                {
                    const newOutput = document.createElement('div');
                    newOutput.classList.add('terminal-line');
                    newOutput.innerHTML = `<span class="terminal-prompt-out"><b>&gt;</b></span>
                    <textarea class="terminal-output" rows="1" readonly></textarea>`;
                    terminalBody.appendChild(newOutput);
                    isLastPromptFilled = true;
                } 
                else {
                    isLastPromptFilled = false;
                }
            }
            
            console.log(isLastPromptFilled);
            const newInputLine = document.createElement('div');
            newInputLine.classList.add('terminal-line');
            newInputLine.innerHTML = `<span class="terminal-prompt-in"><b>&gt;</b></span>
            <textarea class="terminal-input" rows="1" readonly></textarea>`;
            terminalBody.appendChild(newInputLine);
            
            focusLastTextarea(); // Enfocar la última textarea después de crearla
            event.preventDefault(); // Evitar el comportamiento predeterminado del Enter en el textarea
        }
    });

    // Escuchar evento 'input' para ajustar automáticamente la altura del textarea
    terminalBody.addEventListener('input', function(event) {
        const terminalInput = event.target;
        if (terminalInput.classList.contains('terminal-input')) {
            adjustTextareaHeight(terminalInput);
        }
    });

    // Escuchar evento 'copy' para ajustar la altura después de copiar
    terminalBody.addEventListener('copy', function(event) {
        const terminalInput = event.target;
        if (terminalInput.classList.contains('terminal-input')) {
            setTimeout(function() {
                adjustTextareaHeight(terminalInput);
            }, 0);
        }
    });

    // Escuchar evento 'paste' para ajustar la altura después de pegar
    terminalBody.addEventListener('paste', function(event) {
        const terminalInput = event.target;
        if (terminalInput.classList.contains('terminal-input')) {
            setTimeout(function() {
                adjustTextareaHeight(terminalInput);
            }, 0);
        }
    });

    terminalBody.addEventListener('input', function(event) {
        const terminalInput = event.target;
        const rows = Math.floor(terminalInput.scrollHeight / terminalInput.clientHeight)
        if (terminalInput.classList.contains('terminal-input')) {
            if (rows > 1) {
                terminalInput.classList.add('show-scroll'); // Mostrar scroll si es necesario
            } else {
                terminalInput.classList.remove('show-scroll'); // Ocultar scroll si no es necesario
            }
        }
    });

    function createResponseEl(){
        return ;
    }

    function focusLastTextarea() {
        const terminalInputs = terminalBody.querySelectorAll('.terminal-input');
        terminalInputs.forEach((input, index) => {
            if (index === terminalInputs.length - 1) {
                input.removeAttribute('readonly');
                input.focus();
            } else {
                input.setAttribute('readonly', true);
            }
        });
    }

    function adjustTextareaHeight(textarea) {
        textarea.style.height = 'auto';
        textarea.style.height = (textarea.scrollHeight) + 'px';
    }
});
