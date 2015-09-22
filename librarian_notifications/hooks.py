from .notifications import Notification
from .menuitems import NotificationMenuItem


def initialize(supervisor):
    supervisor.exts.notifications = Notification
    supervisor.exts.menuitems.register(NotificationMenuItem)
