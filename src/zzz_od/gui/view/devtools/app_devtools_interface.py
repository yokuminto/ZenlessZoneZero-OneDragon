from qfluentwidgets import qrouter, FluentIcon

from one_dragon.gui.component.interface.pivot_navi_interface import PivotNavigatorInterface
from one_dragon.gui.view.devtools.devtools_screen_area_interface import DevtoolsScreenAreaInterface
from zzz_od.context.zzz_context import ZContext
from zzz_od.gui.view.devtools.devtools_screenshot_switch_interface import DevtoolsScreenshotSwitchInterface


class AppDevtoolsInterface(PivotNavigatorInterface):

    def __init__(self,
                 ctx: ZContext,
                 parent=None):
        self.ctx: ZContext = ctx
        PivotNavigatorInterface.__init__(self, ctx=ctx, object_name='app_devtools_interface', parent=parent,
                                         nav_text_cn='开发工具', nav_icon=FluentIcon.DEVELOPER_TOOLS)

        self.screen_area_interface = DevtoolsScreenAreaInterface(ctx)
        self.screenshot_switch_interface = DevtoolsScreenshotSwitchInterface(ctx)

        self.add_sub_interface(self.screen_area_interface)
        self.add_sub_interface(self.screenshot_switch_interface)
        qrouter.setDefaultRouteKey(self.stacked_widget, self.screenshot_switch_interface.objectName())