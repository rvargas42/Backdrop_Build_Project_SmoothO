import reflex as rx

class chatState(rx.State):
    query: str
    chatHistory: list[tuple[str, str]]

    def handleUpload(self, files: list[rx.UploadFile]):
        pass

    def resizeTextArea(self):
        rx.script("alert('hello world')")

    def resizeContainer(self):
        pass
   