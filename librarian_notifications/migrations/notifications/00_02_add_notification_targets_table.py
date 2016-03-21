SQL = """
create table notification_targets
(
    target_id varchar PRIMARY KEY UNIQUE NOT NULL,      -- id of target rule
    notification_id varchar,
    FOREIGN KEY(notification_id) REFERENCES notifications(notification_id),     -- notification id
    target_type varchar,                                -- type of target to use
    target varchar                                      -- identifying charactaristic of recipient
);
"""


def up(db, conf):
    db.executescript(SQL)
