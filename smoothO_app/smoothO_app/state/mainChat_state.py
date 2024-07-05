import reflex as rx

class ChatState(rx.State):
    query: str
    chatHistory: list[tuple[str, str]]