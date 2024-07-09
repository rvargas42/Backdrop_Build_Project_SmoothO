import reflex as rx

class styles:
    
    chatPageStyle = {
        "chatContainers" : {
            "display":"flex",
            "background-color": "black",
            "height": "100vh",
            "width": "100%",
            "border-width": "1px",
            "border-color": "blue",
        },
        "leftPanel" : {
            "flex": "0 0 30%",
            "background-color": "inherit",
            "height": "99vh",
            "width": "30%",
            "margin-left": "auto",
            "border-width": "1px",
            "border-color": "blue",
        },
        "rightPanel" : {
            "flex":1,
            "height": "99vh",
            "border-width": "1px",
            "border-color": "blue",
            "background-color": "inherit",
            "justifyContent": "space-between",
        },
        "#chatBar" : {
            "flex":1,
            "width":"fill-max",
            "border-width":"1px",
            "border-color": "blue",
        },
        "#chatBar #textArea" : {
            "width":"100%",
            "border-width":"2px",
            "border-color":"blue",
        },

        "displayOutput" : {
            "width":"100%",
            "height":"20vh",
            "border-width": "1px",
            "border-color": "blue",
        },

        "displayDocs" : {
            "max-width": "inherit",
            "max-height":"75%",
            "height":"fit-content",
            "border-width":"1px",
            "border-color":"blue",
        },
        "documentUpload" : {
            "width":"inherit",
            "max-height":"50%",
            "overflow":"hidden",
            "border":"1px dotted",
            "border-color":"red",
        },
    }
