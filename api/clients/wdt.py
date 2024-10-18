from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WDT(BaseApiUI):
    """WTD.List"""
    def list(self, search):
        """Список планов
        :param search:
        :return:
        """

        params = generate_record_list(
            flServerRendering=False,
            iterative_list=True,
            new_navigation=True,
            translit_search=False,
            УчитыватьИерархиюНО=True,
            ФильтрДатаП=('2024-10-31', 'Дата'),
            ФильтрДатаПериод='Период',
            ФильтрДатаС=('2024-10-01', 'Дата'),
            ФильтрДокументНашаОрганизация='-2',
            ФильтрМоиДокументы='Все',
            ФильтрПодтипДокумента=(None, 'Строка'),
            ФильтрПоиска=search,
            ФильтрСостояние='-1'
        )

        return self.client.call_rrecordset(method='WTD.List', **params)

    def delete_timeoff(self, idd):
        """
        Удаление документа
        :param idd:
        """

        self.client.call_rvalue(method='Документ.УдалитьДокументы', ИдО=idd)
