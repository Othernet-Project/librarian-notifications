from .notifications import Notification
from .menuitems import NotificationsMenuItem


def initialize(supervisor):
    supervisor.exts.notifications = Notification
    supervisor.exts.menuitems.register(NotificationsMenuItem)
