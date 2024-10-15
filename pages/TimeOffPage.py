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

    def chech_timeoff(self, **kwargs):
        """Проверка на наличие отгула в реестре"""

        self.list_tgv.row(contains_text=kwargs['Причина']).should_be(Displayed)
        self.list_tgv.row(contains_text=kwargs['Сотрудник']).should_be(Displayed).click()

    def is_deleted_timeoff(self, **kwargs):
        """Проверка на отсутствие отгула в реестре"""

        self.list_tgv.row(contains_text=kwargs['Причина']).should_not_be(Displayed)




