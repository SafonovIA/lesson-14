from atf.ui import *
from controls import *


@templatename('WorkTimeDocuments/timeoff:Dialog')
class Dialog(StackTemplate):
    employee_cl = ControlsLookupInput(By.CSS_SELECTOR, '[data-qa="staff-Lookup__input"]', 'Поиск сотрудника')
    couse_re = RichEditorExtendedEditor(By.CSS_SELECTOR, '[data-qa="wtd-Base__comment"]', 'Причина')
    change_dete_timeoff_elm = Element(By.CSS_SELECTOR, '.wtd-dayTimeSelector--hover-cursor-pointer', 'изменить дату отгула')
    save_btn_db = ExtControlsButtonsDoubleButton(By.CSS_SELECTOR, '[data-qa="edo3-ReadOnlyStateTemplate__saveButton"]', 'Сохранить')
    new_date_timeoff_fild_pd = ControlsCalendarPeriodDialog(SabyBy.DATA_QA, 'controls-PeriodDialog__header-datePickerStart', 'Новая дата отгула', absolute_position=True)
    succes_btn_pd = ControlsCalendarPeriodDialog(By.CSS_SELECTOR, '[data-qa="controls-PeriodDialog__applyButton"]', 'Подтвердить')
    delete_timeoff_btn = ControlsButton(By.CSS_SELECTOR, '[data-qa="deleteDocument"]', "Удалить")

    time_timeoff_elm = Element(By.CSS_SELECTOR, '[title="Указать часы отгула"]', 'Указать часы отгула')
    time_1_elm = ControlsInputTimeInterval(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__start', 'с')
    time_2_elm = ControlsInputTimeInterval(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__end', 'по')

    def fill_timeoff(self, **kwargs):
        """Заполнение формы отгула"""
        self.check_open()

        assert 'Сотрудник_автозаполнение' or 'Сотрудник' and 'Причина' in kwargs.keys(), 'Отсутствуют нужный параметры'

        if 'Сотрудник' in kwargs.keys():
            self.employee_cl.select_from_catalog(kwargs['Сотрудник'])
        if 'Сотрудник_автозаполнение' in kwargs.keys():
            self.employee_cl.autocomplete_search(kwargs['Сотрудник_автозаполнение'])
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
        self.check_close(self.save_btn_db.click)

    def check_filds(self, **kwargs):
        """Проверить заполненные поля"""

        self.check_open()
        self.employee_cl.should_be(ExactText(kwargs.get('Сотрудник_автозаполнение', kwargs.get("Сотрудник"))))
        self.couse_re.should_be(ExactText(kwargs['Причина']))

        if "Дата" in kwargs.keys():
            self.change_dete_timeoff_elm.element('input').should_be(Attribute(value=kwargs['Дата']))
        if "Время" in kwargs.keys():
            tm = kwargs['Время'].split('-')
            self.time_1_elm.should_be(ContainsText(tm[0]))
            self.time_2_elm.should_be(ContainsText(tm[1]))
        self.check_close(self.close_btn.click)
    def delete_timeoff(self):
        """Удалить отгул"""
        self.delete_timeoff_btn.should_be(Displayed).click()
        self.popup_confirmation.confirm(message='Удалить документ?')


