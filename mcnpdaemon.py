import time
import notify2 as n

class mcnpdaemon():
    """
        .. todo:: Make a daemon to watch this, using Flask
    """
    def set_notification_daemon(self, notification):
        notification.show()
        return self

    def run(self):
        i = 0
        while i<10:
            self.check_file()
            time.sleep(5)
            i = i + 1

    def check_file(self):
        print 1
