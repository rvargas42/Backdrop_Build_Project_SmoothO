import reflex as rx
from smoothO_app.styles import styles
from smoothO_app.components.sidebar import sidebar

class welcomeComponents(styles):

    def test(self):
        return rx.script("alert('hello world')"), rx.text("hello world")
    
    def mainContainer(self):
        return rx.container(
            self.test(),
            sidebar(),
        )