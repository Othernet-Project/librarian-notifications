from bottle import request

from librarian_core.contrib.templates.decorators import template_helper

from .notifications import Notification


def to_dict(row):
    return dict((key, row[key]) for key in row.keys())


def get_notifications(db=None):
    db = db or request.db.notifications
    user = request.user.username if request.user.is_authenticated else None
    if user:
        args = [user]
        query = db.Select(sets='notifications',
                          where='(username IS NULL OR username = ?)')
    else:
        args = []
        query = db.Select(sets='notifications', where='username IS NULL')

    query.where += '(dismissable = 0 OR read_at IS NULL)'
    db.query(query, *args)
    for row in db.results:
        notification = Notification(**to_dict(row))
        if not notification.is_read:
            yield notification


def _get_notification_count(db):
    db = db or request.db.notifications
    user = request.user.username if request.user.is_authenticated else None
    if user:
        args = [user]
        query = db.Select('COUNT(*) as count',
                          sets='notifications',
                          where='(username IS NULL OR username = ?)')
    else:
        args = []
        query = db.Select('COUNT(*) as count',
                          sets='notifications',
                          where='username IS NULL')
    query.where += '(dismissable = 0 OR read_at IS NULL)'
    db.query(query, *args)
    unread_count = db.result.count
    unread_count -= len(request.user.options.get('notifications', {}))
    return unread_count


@template_helper
def get_notification_count(db=None):
    key = 'notification_count_{0}'.format(request.session.id)
    count = request.app.supervisor.exts(onfail=None).cache.get(key)
    if count:
        return count

    count = _get_notification_count(db)
    request.app.supervisor.exts.cache.set(key, count)
    return count
