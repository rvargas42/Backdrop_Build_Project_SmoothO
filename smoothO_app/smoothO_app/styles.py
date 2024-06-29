import reflex as rx

class mainChatElements:
    uploadDocumentBox = {
        "display":"flex",
        "border-style":"dotted",
        "margin":"auto",
        "width":"80%",
        "height":"10%",
        "align-items":"center",
    }

    chatBarStyle = {
        "position":"relative",
        "bottom":"0",
    }

class mainChatLayout:
    mainContainer = {
        "border-width":"1px",
        "border-color":"white",
        "height":"100vh",
        "display":"flex",
        "align-items":"center",
	}

    rightPanel = {
        "width": "59%",
        "height":"90vh",
        "display":"flex",
        "border-width":"1px",
        "border-color":"white",
	}

    leftPanel = {
        "width": "41%",
        "height":"90vh",
        "display":"flex",
        "border-width":"1px",
        "border-color":"white",
        "margin":"auto",
	}

    displayOutputContainer = {
        "height": "45rem",
        "border-width":"1px",
        "border-color":"white",
        "margin":"auto",
    }

    chatBarContainer = {
        "border-width":"1px",
        "border-color":"white",
        "display":"flex",
        "margin-top": "auto",
        "bottom":"0",
    }