import datetime
import logging

from librarian_core.utils import utcnow


def notification_cleanup(db, default_expiry):
    logging.debug("Notification cleanup started.")
    now = utcnow()
    auto_expires_at = now - datetime.timedelta(seconds=default_expiry)
    q = db.Delete('notifications', where='dismissable = true')
    q.where += ('((expires_at IS NULL AND created_at <= %(auto_expires_at)s) '
                'OR expires_at <= %(now)s)')
    rowcount = db.execute(q, dict(now=now, auto_expires_at=auto_expires_at))
    logging.debug("Notification cleanup deleted: {} "
                  "notifications.".format(rowcount))
