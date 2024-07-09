import reflex as rx

class googleAuthProvider(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleAuthProvider"

    clientId : rx.Var[str]

class GoogleLogin(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleLogin"

    on_success: rx.EventHandler[lambda data: [data]]