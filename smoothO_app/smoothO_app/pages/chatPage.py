import reflex as rx
from smoothO_app.components import mainChat

@rx.page("/")
def chatPage():

    pageComponents = mainChat.mainChatComponents()
    chatBar = pageComponents.chatBar()
    return rx.container(
        rx.vstack(
            chatBar,
        ),
    )