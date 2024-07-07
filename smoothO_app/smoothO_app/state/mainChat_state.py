import reflex as rx
from styles import styles

class uploadDocState(rx.State):
    pass

class chatState(rx.State):
    query: str
    chatHistory: list[tuple[str, str]]

class styleChanges(rx.State):
    
    def resizeTextArea(self):
        pass


    def resizeContainer(self):
        pass