import reflex as rx
from smoothO_app.styles import mainChatElements, mainChatLayout

class mainChatComponents():
	'''class containing components for the main chat page'''
	
	def activeTools(self):
		pass

	def uploadNewDoc(self):
		return rx.upload(
			rx.text("Drag and drop files here or click to select files"),
			id="documentUpload",
			style=mainChatElements.uploadDocumentBox
		)

	def displayDocs(self):
		'''
		This method returns a component consisting of a side bar that emulates file system to view uploaded files
		'''
		pass

	def chatBar(self):
		return rx.input(placeholder="Talk with your knowledge base...", style=mainChatElements.chatBarStyle)
	
	def displayOutput(self):
		return rx.scroll_area(
			rx.flex(
				rx.text(id="LLMResponse"), 
				direction="column",
				spacing="4"
			),
			type="always",
    		scrollbars="vertical",
    		style=mainChatLayout.displayOutputContainer,
		)
	
	def mainContainer(self):
		'''
		This method is the only one to be called and returns the general layout of a page content
		'''
		return rx.hstack(
			rx.container(self.uploadNewDoc(), style=mainChatLayout.leftPanel),
			rx.container(
				rx.container(self.displayOutput()),
				rx.container(self.chatBar(), style=mainChatLayout.chatBarContainer),
				style=mainChatLayout.rightPanel,
			),
			style=mainChatLayout.mainContainer,
		)