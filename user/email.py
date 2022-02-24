"""

"""

import threading

class EmailThread(threading.Thread):
    def __init__(self, email_message) -> None:
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.email_message.send()