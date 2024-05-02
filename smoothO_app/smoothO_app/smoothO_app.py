import reflex as rx
from .pages import chatPage


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="small", accent_color="teal"
    )
)