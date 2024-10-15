from atf.ui import *
from controls import *


class TimeOff(Region):
    """Реестр 'документы' """

    create_btn = ExtControlsDropdownAddButton(SabyBy.DATA_QA, 'sabyPage-addButton', 'Создать отгул')
    list_tgv = ControlsTreeGridView(By.CSS_SELECTOR, '.edo3-Browser [data-qa="gridWrapper"]', 'Список отгулов')

    def create_document(self, fisrst_pos='Отгул', second_pos='Отгул'):
        """
            Создание документа
            :param second_pos: Выбрать нужный раздел
            :param fisrst_pos:  Выбрать нужный документ
        """

        from pages.timeoff import Dialog

        self.create_btn.select(fisrst_pos, second_pos)
        timeoff_card = Dialog(self.driver)
        timeoff_card.check_open()
        return timeoff_card

    def open_timeoff(self, couse):
        """Открыть отгул"""

        self.list_tgv.row(contains_text=couse).click()

    def exist_timeoff(self, couse, exist=True):
        """Проверка на отсутствие отгула в реестре"""
        if exist:
            self.list_tgv.row(contains_text=couse).should_be(Displayed)
        else:
            self.list_tgv.row(contains_text=couse).should_not_be(Displayed)





