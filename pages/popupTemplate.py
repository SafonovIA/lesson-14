from atf.ui import *
from controls import *


@templatename('WorkTimeDocuments/timeoff:Dialog')
class Dialog(DialogTemplate):
    succses_panel_pc = ControlsPopupConfirmation(By.CSS_SELECTOR, '.controls-ConfirmationTemplate__body', 'Панель подтверждения')