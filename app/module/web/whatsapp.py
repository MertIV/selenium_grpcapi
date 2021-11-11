from app.module.web.base import Website,By
import threading
import time

class WWeb(Website):
    def __init__(self, *args, **kwargs) -> None:
        super(WWeb, self).__init__(*args, **kwargs)

    def main_page(self):
        self.go_to("https://web.whatsapp.com/")

    def get_qr(self):
        while True:
            # #every 15 seconds refresh and send qr
            # threading.Timer(15.0, self.get_qr).start()
            self.main_page()

            qr = self.get_element_wait("div[data-ref]",by=By.CSS_SELECTOR)
            value = self.get_attribute(qr,"data-ref")
            time.sleep(15)

            return(value)

ww = WWeb()
value = ww.get_qr()
print(value)
