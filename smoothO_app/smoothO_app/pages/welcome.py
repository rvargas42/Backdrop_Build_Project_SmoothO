import reflex as rx
from smoothO_app.components import welcome
from smoothO_app.styles import styles

"""
Code implementing a simple welcome page where to login or signup
"""

@rx.page("/")
def welcomePage():
    pageComponents = welcome.welcomeComponents()
    content = pageComponents.mainContainer()
    return content