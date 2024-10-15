from datetime import datetime, timedelta
from atf import *
from atf.ui import *
from pages.AuthPages import AuthPage
from pages.TimeOffPage import TimeOff


class Test(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth()

    def setUp(self):
        self.timeoff_page = TimeOff(self.driver)
        self.timeoff_card = self.timeoff_page.create_document('Отгул', 'Отгул')

    def tearDown(self):
        self.timeoff_card.fill_timeoff(**self.data_timeoff)
        self.timeoff_card.save_timeoff()
        self.timeoff_page.chech_timeoff(**self.data_timeoff)
        self.timeoff_card.check_filds(**self.data_timeoff)
        self.timeoff_card.delete_timeoff()
        self.timeoff_page.is_deleted_timeoff(**self.data_timeoff)
        self.browser.close_windows_and_alert()

    def test_01_create_timeoff(self):
        """Создание и удаление отгула"""
        tomorrow = datetime.strftime(datetime.today() + timedelta(days=1), '%d.%m.%y')
        self.data_timeoff = {
            "Сотрудник": 'Регламентные События',
            "Причина": "Причина отгула",
            "Дата": tomorrow
        }

    def test_02_create_timeoff(self):
        """Второй вариант сохдание отгула"""
        tomorrow = datetime.strftime(datetime.today() + timedelta(days=1), '%d.%m.%y')
        self.data_timeoff = {
            "Сотрудник": 'Регламентные События',
            "Причина": "Причина отгула",
            "Дата": tomorrow,
            "Время": '12:00-14:00'
        }
