import reflex as rx

class styles:
    
    chatPageStyle = {
        "chatContainers" : {
            "display":"flex",
            "background-color": "black",
            "height": "99vh",
            "width": "100%",
            "border-width": "1px",
            "border-color": "blue",
        },
        "leftPanel" : {
            "display":"flex",
            "background-color": "inherit",
            "height": "inherit",
            "margin-left": "auto",
            "max-width":" fit-content",
            "border-width": "1px",
            "border-color": "blue",
        },
        "rightPanel" : {
            "display":"flex",
            "background-color": "inherit",
            "height": "inherit",
            "max-width": "50%",
            "margin-left": "0px",
            "align-items": "center",
            "border-width": "1px",
            "border-color": "blue",
        },
        "#chatBar" : {
            "height":"fit-content",
            "width": "100%",
            "border-width":"1px",
            "border-color": "blue",
        },
        "#chatBar #textArea" : {
            "width":"100%",
            "resize":"none",
            "overflow":"hidden",
            "border-width":"2px",
            "border-color":"blue",
        },

        "displayOutput" : {
            "height": "40rem",
            "width": "100%",
            "margin-bottom":"10%",
            "padding-bottom":"10px",
            "border-width": "1px",
            "border-color": "blue",
        },
        "displayDocs" : {
            
        },
        "documentUpload" : {
            "display": "flex",
            "max-width": "fit-content",
        },
        ".resizer": {
            "width": "10px",
            "background": "#ccc",
            "cursor": "ew-resize",
            "position": "absolute",
            "right": "0",
            "top": "0",
            "bottom": "0",
        }
    }
