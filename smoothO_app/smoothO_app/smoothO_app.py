import reflex as rx
from .pages import chatPage


app = rx.App(
    stylesheets=[
        "/css/chatPageStyles.css",
    ],
    head_components=[
        rx.script("/scripts/chatPageMain.js"),
    ]
)