import reflex as rx

class mainChatComponents:
    '''class containing components for the main chat page'''
    
    def activeTools(self):
        pass
    def uploadNewDoc(self):
        pass
    def displayDocs(self):
        '''
        This method returns a component consisting of a side bar that emulates file system to view uploaded files
        '''
        pass
    def chatBar(self):
        return rx.input(placeholder="Talk with your knowledge base...", max_length="20")
    def displayOutput(self):
        pass