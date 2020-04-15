import datetime
from base_page import BasePage, parameter_no_more_changing


class MainPage(BasePage):

    def open(self):
        self.browser.get(self.url)

    def wait_for_counter_disappear(self, how, what):
        assert self.is_disappeared(how, what), "Счетчик не пропадает"
        print("Счетчик пропал")

    def watch_the_wheel(self, browser, how, what):
        # Следим за рулеткой, если значение перестало меняться
        assert parameter_no_more_changing(browser, how, what), "Рулетка не останавливается слишком долгое время"
        print("Рулетка остановилась")

    def collect_data(self, browser, how, what):
        result = browser.find_element(how, what).get_attribute("class").split()
        # получает строку вида "inline-block w-24 h-24 rounded-full ml-1 coin-ct"

        result = str(result.pop(5))
        now = datetime.datetime.now()
        # coin-ct - black
        # coin-t- yellow
        # coin-bonus - bonus

        if result == "coin-ct":
            result = "black"
        elif result == "coin-t":
            result = "yellow"
        elif result == "coin-bonus":
            result = "bonus"

        print(str(now.strftime("%d-%m-%Y %H:%M:%S")) + " | " + result + "\n")

        log_file = open("log_file.txt", "a", )
        try:
            log_file.write(str(now.strftime("%d-%m-%Y %H:%M:%S")) + " | " + result + "\n")
        finally:
            log_file.close()

    # def wait_for_counter(self, how, what):
    #     assert self.is_element_present(how, what), "Счетчик не появляется"
    #     print("Счетчик появился")




