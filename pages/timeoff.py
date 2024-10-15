from atf.ui import *
from controls import *


@templatename('WorkTimeDocuments/timeoff:Dialog')
class Dialog(DocumentTemplate):
    employee_cl = ControlsLookupInput(By.CSS_SELECTOR, '[data-qa="staff-Lookup__input"]', 'Поиск сотрудника')
    couse_re = RichEditorExtendedEditor(By.CSS_SELECTOR, '[data-qa="wtd-Base__comment"]', 'Причина')
    change_dete_timeoff_elm = Element(By.CSS_SELECTOR, '.wtd-dayTimeSelector--hover-cursor-pointer', 'изменить дату отгула')
    save_btn_db = ExtControlsButtonsDoubleButton(By.CSS_SELECTOR, '[data-qa="edo3-ReadOnlyStateTemplate__saveButton"]', 'Сохранить')
    new_date_timeoff_fild_pd = ControlsCalendarPeriodDialog(SabyBy.DATA_QA, 'controls-PeriodDialog__header-datePickerStart', 'Новая дата отгула', absolute_position=True)
    succes_btn_pd = ControlsCalendarPeriodDialog(By.CSS_SELECTOR, '[data-qa="controls-PeriodDialog__applyButton"]', 'Подтвердить')
    delete_timeoff_btn = ControlsButton(By.CSS_SELECTOR, '[data-qa="deleteDocument"]', "Удалить")
    succses_panel_pc = ControlsPopupConfirmation(By.CSS_SELECTOR, '.controls-ConfirmationTemplate__body', 'Панель подтверждения', absolute_position=True)

    time_timeoff_elm = Element(By.CSS_SELECTOR, '[title="Указать часы отгула"]', 'Указать часы отгула')
    time_1_elm = ControlsInputTimeInterval(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__start', 'с')
    time_2_elm = ControlsInputTimeInterval(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__end', 'по')

    def fill_timeoff(self, **kwargs):
        """Заполнение формы отгула"""

        if 'Сотрудник' and 'Время' in kwargs.keys():
            self.employee_cl.select_from_catalog(kwargs['Сотрудник'])
        elif 'Сотрудник' in kwargs.keys():
            self.employee_cl.autocomplete_search(kwargs['Сотрудник'])

        if "Причина" in kwargs.keys():
            self.couse_re.type_in(kwargs['Причина'])

        if "Дата" in kwargs.keys():
            self.change_dete_timeoff_elm.click()
            self.new_date_timeoff_fild_pd.should_be(Displayed).type_start(kwargs['Дата'])
            self.succes_btn_pd.click()
            self.new_date_timeoff_fild_pd.should_not_be(Displayed)
        if 'Время' in kwargs.keys():
            self.time_timeoff_elm.click()
            tm = kwargs['Время'].split('-')
            self.time_1_elm.type_in(tm[0], human=True)
            self.time_2_elm.type_in(tm[1], human=True)

    def save_timeoff(self):
        """Сохранить отгул"""

        self.save_btn_db.click()
        self.save_btn_db.should_not_be(Displayed)

    def check_filds(self, test_2=False, **kwargs):
        """Проверить заполненные поля"""

        if 'Сотрудник' in kwargs.keys():
            self.employee_cl.should_be(Displayed, ExactText(kwargs['Сотрудник']))
        if "Причина" in kwargs.keys():
            self.couse_re.should_be(Displayed, ExactText(kwargs['Причина']))
        if "Дата" in kwargs.keys():
            self.change_dete_timeoff_elm.element('input').should_be(Attribute(value=kwargs['Дата']))
        if test_2:
            self.time_timeoff_elm.click()
            self.time_1_elm.type_in("12:00", human=True)
            self.time_2_elm.type_in("14:00", human=True)

    def delete_timeoff(self):
        """Удалить отгул"""
        self.delete_timeoff_btn.should_be(Displayed)
        self.delete_timeoff_btn.click()

        self.succses_panel_pc.should_be(Displayed).confirm()
        self.succses_panel_pc.should_not_be(Displayed)


