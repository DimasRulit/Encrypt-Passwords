import win32clipboard
class SetToClip:
    def __init__(self,text):
        self.text = text
        self.set_clipboard_text()
    def set_clipboard_text(self):
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(self.text)
        finally:
            win32clipboard.CloseClipboard()