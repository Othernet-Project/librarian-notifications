"""
notifications.py: routes related to notifications

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import datetime

from bottle import request
from bottle_utils.ajax import roca_view

from librarian_core.contrib.templates.renderer import template

from .helpers import get_notifications
from .notifications import NotificationGroup


@roca_view('notification_list', '_notification_list', template_func=template)
def notification_list():
    key = 'notification_group_{0}'.format(request.session.id)
    if request.app.supervisor.exts.is_installed('cache'):
        groups = request.app.supervisor.exts.cache.get(key)
        if groups:
            return dict(groups=groups)

    groups = NotificationGroup.group_by(get_notifications(),
                                        by=('category', 'read_at'))
    request.app.supervisor.exts.cache.set(key, groups)
    return dict(groups=groups)


def mark_read(notifications):
    now = datetime.datetime.now()
    for notification in notifications:
        if notification.dismissable:
            notification.mark_read(now)


@roca_view('notification_list', '_notification_list', template_func=template)
def notifications_read():
    category = request.forms.get('category')
    # needs None instead of empty string to compare against null columns
    read_at = request.forms.get('read_at') or None
    groups = NotificationGroup.group_by(get_notifications(),
                                        by=('category', 'read_at'))
    for group in groups:
        if not category or (group.category == category and
                            group.read_at == read_at):
            mark_read(group.notifications)
            break

    for key_tmpl in ('notification_group_{0}', 'notification_count_{0}'):
        key = key_tmpl.format(request.session.id)
        request.app.supervisor.exts.cache.delete(key)

    return dict(groups=[grp for grp in groups if not grp.is_read])


def routes(app):
    return (
        ('notifications:list', notification_list,
         'GET', '/notifications/', {}),
        ('notifications:read', notifications_read,
         'POST', '/notifications/', {}),
    )
