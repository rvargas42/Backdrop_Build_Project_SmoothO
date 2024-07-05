import reflex as rx

class mainChatComponents():
	'''class containing components for the main chat page'''
	
	def activeTools(self):
		pass

	def uploadNewDoc(self):
		return rx.upload(
			rx.text("Drag and drop files here or click to select files"),
			id="documentUpload",
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
			id="displayDocs",
		)

	def chatBar(self):
		return rx.input(placeholder="Talk with your knowledge base...")
	
	def displayOutput(self):
		return rx.scroll_area(
			rx.flex(
				rx.text(id="LLMResponse"), 
				direction="column",
				spacing="4"
			),
			type="always",
    		scrollbars="vertical",
			id="displayOutput",
		)
	
	def mainContainer(self):
		'''
		This method is the only one to be called and returns the general layout of a page content
		'''
		return rx.hstack(
			rx.container(
				self.uploadNewDoc(),
				self.displayDocs(),
				id="leftPanel",
			),
			rx.container(
				rx.container(self.displayOutput()),
				rx.container(self.chatBar()),
				id="rightPanel",
			),
			id="chatContainers"
		)