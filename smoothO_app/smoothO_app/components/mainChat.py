import reflex as rx
from smoothO_app.styles import mainChatElements, mainChatLayout

class mainChatComponents():
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
		return rx.input(placeholder="Talk with your knowledge base...", max_length="20", style=mainChatElements.chatBarStyle)
	
	def displayOutput(self):
		return rx.box(
			"CSS color",
    	),
	
	def mainContainer(self):
		'''
		This method is the only one to be called and returns the general layout of a page content
		'''
		return rx.hstack(
			rx.container(style=mainChatLayout.leftPanel),
			rx.container(
				rx.container(self.displayOutput(), style=mainChatLayout.displayOutputContainer),
				rx.container(self.chatBar(), style=mainChatLayout.chatBarContainer),
				style=mainChatLayout.rightPanel,
			),
			style=mainChatLayout.mainContainer,
		)