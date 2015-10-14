<%def name="default(group)">
    % for item in group.notifications:
        <p class="message">${item.safe_message()}</p>
    % endfor
</%def>
<%def name="content(group)">
    <h2 class="description">${ngettext('A content item has been added to the Library with the following title:',
                                       '{count} content items have been added to the Library with the following titles:',
                                       group.count).format(count=group.count)}</h2>
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
        <li class="notification h-bar ${loop.cycle('white', '')} ${'' if group.is_read else 'unread'}">
            % if not group.is_read:
            <span class="alert">
                <span class="icon${' dismissable' if group.dismissable else ''}"></span>
            </span>
            % endif
            ${h.form('post', _class="notification-body")}
                <input type="hidden" name="category" value="${group.category}" />
                <input type="hidden" name="read_at" value="${group.read_at if group.read_at else ''}" />
                <div class="message">${notification_templates.get(group.category, default_template)(group)}</div>
                <span class="timestamp">${group.created_at.date()}</span>
                <span class="icon ${group.category}"></span>
                % if not group.is_read:
                <button class="small" type="submit">${_('Dismiss')}</button>
                % endif
            </form>
        </li>
        % endfor
    </ul>
% else:
    ${request.app.supervisor.exts.notifications.send('Poor you, heres a notification for you')}
    <p class="empty">
        ## Translators, note that appears on notifications page when there are no new notifications
        ${_('There are no new notifications')}
    </p>
% endif
