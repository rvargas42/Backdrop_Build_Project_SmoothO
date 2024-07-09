import reflex as rx
from smoothO_app.state.mainChat_state import chatState
from smoothO_app.components.navbar import navbar_buttons



class mainChatComponents():
	'''class containing components for the main chat page'''

	def activeTools(self):
		return rx.vstack(
		)

	def uploadNewDoc(self):
		return rx.upload(
			rx.text("Drag and drop files here or click to select files"),
			id="",
		)

	def displayDocs(self):
		'''
		This method returns a component consisting of a side bar that emulates file system to view uploaded files
		'''
		return rx.scroll_area(
			rx.flex(

			),
			type="always",
    		scrollbars="vertical",
			id="",
		)

	def chatBar(self):
		return rx.container(
			rx.text_area(
				placeholder="Talk with your knowledge base...",
				id="textArea",
				on_change=chatState.resizeTextArea(),
			),
			id="chatBar",
		)
	
	def displayOutput(self):
		return rx.container(
			rx.scroll_area(
				rx.flex(
					rx.text(id="LLMResponse"), 
					direction="column",
					spacing="4"
				),
				type="always",
				scrollbars="vertical",
			),
			id="displayOutput",
		)
	
	def mainContainer(self):
		'''
		This method is the only one to be called and returns the general layout of a page content
		'''
		return rx.vstack(
			rx.hstack(
				rx.script(src="/scripts/chatPageMain.js"),
				rx.container(
					self.uploadNewDoc(),
					self.displayDocs(),
					id="leftPanel",
				),
				rx.container(
					self.displayOutput(),
					self.chatBar(),
					id="rightPanel",
				),
				id="chatContainers"
			)
		)