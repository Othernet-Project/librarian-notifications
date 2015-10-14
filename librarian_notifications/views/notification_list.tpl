<%inherit file='/narrow_base.tpl'/>
<%namespace name='notification_list' file='_notification_list.tpl'/>

<%block name="title">
## Translators, used as page title
${_('Messages')}
</%block>

% if groups:
<div class="h-bar">
    <div class="form actions">
        <form method="post">
            <h2>
                <span class="icon icon-message-alert"></span> 
                ${_('Messages')}
            </h2>
            <p class="subtitle-buttons">
                <button name="action" value="mark_read_all" class="clean" tabindex="1">
                    <span class="icon icon-no-outline"></span>
                    ## Translators, used as label for discarding all unread notifications
                    <span>${_('Mark all as read')}</span>
                </button>
            </p>
        </form>
    </div>
</div>
% endif

${notification_list.body()}
