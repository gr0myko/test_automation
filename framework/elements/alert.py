class Alert:
    def __init__(self, alert):
        self.alert = alert

    def get_text(self):
        return self.alert.text

    def send_text_to_alert(self, text):
        self.alert.send_keys(text)

    def accept(self):
        self.alert.accept()

    def dismiss(self):
        self.alert.dismiss()
