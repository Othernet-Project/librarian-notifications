from .notifications import Notification


def initialize(supervisor):
    supervisor.exts.notifications = Notification

    def invalidate_notification_cache(notification):
        # for now jsut invalidate the whole cache, no matter if it's a
        # private notification
        for key in ('notification_group', 'notification_count'):
            supervisor.exts.cache.invalidate(key)

    Notification.on_send(invalidate_notification_cache)
