from datetime import datetime, timedelta
from atf.ui import *
from pages.AuthPages import AuthPage
from pages.TimeOffPage import TimeOff
from random import randint
from atf.api.json_rpc import JsonRpcClient
from api.wrappers.time_off_api_wrapper import TimeoffApiWrapper


class Test(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient(url=cls.config.get('SITE'), verbose_log=2)
        cls.client.auth(login=cls.config.get("LOGIN"), password=cls.config.get("PASSWORD"))
        cls.wdt = TimeoffApiWrapper(cls.client)

        AuthPage(cls.driver).auth()
        cls.tomorrow = datetime.strftime(datetime.today() + timedelta(days=1), '%d.%m.%y')

    def setUp(self):
        self.browser.open('https://fix-online.sbis.ru/page/work-schedule-documents')
        self.timeoff_page = TimeOff(self.driver)
        self.timeoff_card = self.timeoff_page.create_document('Отгул', 'Отгул')

    def tearDown(self):
        self.browser.close_windows_and_alert()

    def test_01_create_timeoff(self):
        """Создание и удаление отгула"""

        data_timeoff = {
            "Сотрудник_автозаполнение": 'Регламентные События',
            "Причина": f"Причина отгула {randint(1000, 10000)}",
            "Дата": self.tomorrow
        }
        self.timeoff_card.fill_timeoff(**data_timeoff)
        self.timeoff_card.save_timeoff()
        self.timeoff_page.exist_timeoff(data_timeoff['Причина'])
        self.timeoff_page.open_timeoff(data_timeoff['Причина'])
        self.timeoff_card.check_filds(**data_timeoff)
        self.wdt.delete_document(data_timeoff['Причина'], data_timeoff["Сотрудник_автозаполнение"])
        self.browser.refresh()
        self.timeoff_page.exist_timeoff(data_timeoff['Причина'], exist=False)

    def test_02_create_timeoff(self):
        """Второй вариант сохдание отгула"""

        data_timeoff = {
            "Сотрудник": 'Регламентные События',
            "Причина": f"Причина отгула {randint(1000, 10000)}",
            "Дата": self.tomorrow,
            "Время": '12:00-14:00'
        }
        self.timeoff_card.fill_timeoff(**data_timeoff)
        self.timeoff_card.save_timeoff()
        self.timeoff_page.exist_timeoff(data_timeoff['Причина'])
        self.timeoff_page.open_timeoff(data_timeoff['Причина'])
        self.timeoff_card.check_filds(**data_timeoff)
        self.wdt.delete_document(data_timeoff['Причина'], data_timeoff["Сотрудник"])
        self.browser.refresh()
        self.timeoff_page.exist_timeoff(data_timeoff['Причина'], exist=False)