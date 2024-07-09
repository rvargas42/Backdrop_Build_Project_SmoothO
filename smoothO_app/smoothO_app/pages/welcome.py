import reflex as rx
from smoothO_app.components import welcome

"""
Code implementing a simple welcome page where to login or signup
"""

@rx.page("/")
def welcomePage():
    pageComponents = welcome.welcomeComponents()
    content = pageComponents.mainContainer()
    return content