from qfluentwidgets import FluentIcon

from one_dragon.gui.component.interface.pivot_navi_interface import PivotNavigatorInterface
from zzz_od.context.zzz_context import ZContext
from zzz_od.gui.view.game_assistant.life_on_line_run_interface import LifeOnLineRunInterface


class GameAssistantInterface(PivotNavigatorInterface):

    def __init__(self,
                 ctx: ZContext,
                 parent=None):
        self.ctx: ZContext = ctx
        PivotNavigatorInterface.__init__(self, object_name='game_assistant_interface', parent=parent,
                                         nav_text_cn='游戏助手', nav_icon=FluentIcon.HELP)

    def create_sub_interface(self):
        """
        创建下面的子页面
        :return:
        """
        self.add_sub_interface(LifeOnLineRunInterface(self.ctx))