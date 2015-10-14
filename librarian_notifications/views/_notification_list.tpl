<%def name="default(group)">
    % for item in group.notifications:
        <p class="message">${item.safe_message()}</p>
    % endfor
</%def>
<%def name="content(group)">
    <h3 class="description">
        ${ngettext('A content item has been added to the Library with the following title:',
        '{count} content items have been added to the Library with the following titles:',
        group.count).format(count=group.count)}
    </h3>
    <p class="titles">${', '.join([item.safe_message('title') for idx, item in enumerate(group.notifications) if idx < 20])}</p>
</%def>

<% 
    notification_templates = {
        'default': default,
        'content': content,
    }
    default_template = default
%>

% if groups:
    <ul id="notification-list" class="notification-list">
        % for group in groups:
            <li class="notification">
            <form method="post" action="${i18n_url('notifications:list')}">
                <input type="hidden" name="category" value="${group.category}" />
                <input type="hidden" name="read_at" value="${group.read_at if group.read_at else ''}" />
                <div class="notification-body">
                    <div class="message">${notification_templates.get(group.category, default_template)(group)}</div>
                    <p class="notification-meta">
                        <span class="notification-icon ${group.category}"></span>
                        <span class="timestamp">${group.created_at.date()}</span>
                    </p>
                </div>
                % if not group.is_read:
                    <button class="notification-delete clean" type="submit" tabindex="${loop.index + 2}">
                        <span class="icon icon-no"></span>
                        <span class="notification-delete-label">${_('Dismiss')}</span>
                    </button>
                % endif
                </form>
            </li>
        % endfor
    </ul>
% else:
    <p class="empty">
        ## Translators, note that appears on notifications page when there are no new notifications
        ${_('There are no new notifications')}
    </p>
% endif
