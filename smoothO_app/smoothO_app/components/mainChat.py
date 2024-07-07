import reflex as rx
from smoothO_app.styles import styles

class mainChatComponents(styles):
	'''class containing components for the main chat page'''
	
	def activeTools(self):
		pass

	def uploadNewDoc(self):
		return rx.upload(
			rx.text("Drag and drop files here or click to select files"),
			style=self.chatPageStyle["documentUpload"]
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
			style=self.chatPageStyle["displayDocs"]
		)

	def chatBar(self):
		return rx.container(
			rx.text_area(
				placeholder="Talk with your knowledge base...",
				style=self.chatPageStyle["#chatBar #textArea"],
				id="textArea"
			),
			style=self.chatPageStyle["#chatBar"],
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
			style=self.chatPageStyle["displayOutput"],
		)
	
	def mainContainer(self):
		'''
		This method is the only one to be called and returns the general layout of a page content
		'''
		return rx.hstack(
			rx.script(src="/scripts/chatPageMain.js"),
			rx.container(
				self.uploadNewDoc(),
				self.displayDocs(),
				style=self.chatPageStyle["leftPanel"]
			),
			rx.container(
				self.displayOutput(),
				self.chatBar(),
				style=self.chatPageStyle["rightPanel"],
			),
			style=self.chatPageStyle["chatContainers"],
		)