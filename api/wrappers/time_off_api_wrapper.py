from atf.api.base_api_ui import BaseApiUI
from atf import *
from api.clients.wdt import WDT


class TimeoffApiWrapper(BaseApiUI):
    """WTD.List"""

    def __init__(self, client):
        super().__init__(client)
        self.timeoff_api = WDT(client)

    def delete_document(self, timeoff_mask, search):
        """
        Удаление документа
        :param timeoff_mask:
        :param search:
        """

        assert timeoff_mask, 'Параметр timeoff_mask не может быть пустым'
        response = self.timeoff_api.list(search).result
        for i in response:
            if timeoff_mask == i['NoteText']:
                self.timeoff_api.delete_timeoff(i['DocID'])