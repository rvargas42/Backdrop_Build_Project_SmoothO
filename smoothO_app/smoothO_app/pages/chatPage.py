import reflex as rx
from smoothO_app.components import mainChat


"""
All code refering to the main chat page app
"""

@rx.page("/chat")
def chatPage():
    '''
    Layout for this page are three main containers:
    1 for chat input, another for chat output and another for file management
    '''
    #instanciating all components for this page
    pageComponents = mainChat.mainChatComponents()
    #Content var will contain a main container with a layout designed in the components module
    content = pageComponents.mainContainer()
    return content