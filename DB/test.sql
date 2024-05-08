--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.3 в Пн май 6 19:36:45 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: auth_group
CREATE TABLE IF NOT EXISTS auth_group (
    id   INTEGER       NOT NULL
                       PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (150) NOT NULL
                       UNIQUE
);


-- Таблица: auth_group_permissions
CREATE TABLE IF NOT EXISTS auth_group_permissions (
    id            INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    group_id      INTEGER NOT NULL
                          REFERENCES auth_group (id) DEFERRABLE INITIALLY DEFERRED,
    permission_id INTEGER NOT NULL
                          REFERENCES auth_permission (id) DEFERRABLE INITIALLY DEFERRED
);


-- Таблица: auth_permission
CREATE TABLE IF NOT EXISTS auth_permission (
    id              INTEGER       NOT NULL
                                  PRIMARY KEY AUTOINCREMENT,
    content_type_id INTEGER       NOT NULL
                                  REFERENCES django_content_type (id) DEFERRABLE INITIALLY DEFERRED,
    codename        VARCHAR (100) NOT NULL,
    name            VARCHAR (255) NOT NULL
);


-- Таблица: auth_user
CREATE TABLE IF NOT EXISTS auth_user (
    id           INTEGER       NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    password     VARCHAR (128) NOT NULL,
    last_login   DATETIME,
    is_superuser BOOL          NOT NULL,
    username     VARCHAR (150) NOT NULL
                               UNIQUE,
    first_name   VARCHAR (150) NOT NULL,
    last_name    VARCHAR (150) NOT NULL,
    is_staff     BOOL          NOT NULL,
    is_active    BOOL          NOT NULL,
    date_joined  DATETIME      NOT NULL,
    email        VARCHAR (254) NOT NULL
);


-- Таблица: auth_user_groups
CREATE TABLE IF NOT EXISTS auth_user_groups (
    id       INTEGER NOT NULL
                     PRIMARY KEY AUTOINCREMENT,
    user_id  INTEGER NOT NULL
                     REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    group_id INTEGER NOT NULL
                     REFERENCES auth_group (id) DEFERRABLE INITIALLY DEFERRED
);


-- Таблица: auth_user_user_permissions
CREATE TABLE IF NOT EXISTS auth_user_user_permissions (
    id            INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    user_id       INTEGER NOT NULL
                          REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    permission_id INTEGER NOT NULL
                          REFERENCES auth_permission (id) DEFERRABLE INITIALLY DEFERRED
);


-- Таблица: django_admin_log
CREATE TABLE IF NOT EXISTS django_admin_log (
    id              INTEGER             NOT NULL
                                        PRIMARY KEY AUTOINCREMENT,
    action_time     DATETIME            NOT NULL,
    object_id       TEXT,
    object_repr     VARCHAR (200)       NOT NULL,
    change_message  TEXT                NOT NULL,
    content_type_id INTEGER
                                        REFERENCES django_content_type (id) DEFERRABLE INITIALLY DEFERRED,
    user_id         INTEGER             NOT NULL
                                        REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    action_flag     [SMALLINT UNSIGNED] NOT NULL
                                        CHECK ("action_flag" >= 0) 
);


-- Таблица: django_content_type
CREATE TABLE IF NOT EXISTS django_content_type (
    id        INTEGER       NOT NULL
                            PRIMARY KEY AUTOINCREMENT,
    app_label VARCHAR (100) NOT NULL,
    model     VARCHAR (100) NOT NULL
);


-- Таблица: django_migrations
CREATE TABLE IF NOT EXISTS django_migrations (
    id      INTEGER       NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    app     VARCHAR (255) NOT NULL,
    name    VARCHAR (255) NOT NULL,
    applied DATETIME      NOT NULL
);


-- Таблица: django_session
CREATE TABLE IF NOT EXISTS django_session (
    session_key  VARCHAR (40) NOT NULL
                              PRIMARY KEY,
    session_data TEXT         NOT NULL,
    expire_date  DATETIME     NOT NULL
);


-- Таблица: Incidents_incidents
CREATE TABLE IF NOT EXISTS Incidents_incidents (
    id             INTEGER       NOT NULL
                                 PRIMARY KEY AUTOINCREMENT,
    address        VARCHAR (255) NOT NULL,
    description    VARCHAR (255) NOT NULL,
    latitude       REAL          NOT NULL,
    longitude      REAL          NOT NULL,
    taken_measures VARCHAR (255) 
);


-- Индекс: auth_group_permissions_group_id_b120cbf9
CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions (
    "group_id"
);


-- Индекс: auth_group_permissions_group_id_permission_id_0cd325b0_uniq
CREATE UNIQUE INDEX IF NOT EXISTS auth_group_permissions_group_id_permission_id_0cd325b0_uniq ON auth_group_permissions (
    "group_id",
    "permission_id"
);


-- Индекс: auth_group_permissions_permission_id_84c5c92e
CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions (
    "permission_id"
);


-- Индекс: auth_permission_content_type_id_2f476e4b
CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b ON auth_permission (
    "content_type_id"
);


-- Индекс: auth_permission_content_type_id_codename_01ab375a_uniq
CREATE UNIQUE INDEX IF NOT EXISTS auth_permission_content_type_id_codename_01ab375a_uniq ON auth_permission (
    "content_type_id",
    "codename"
);


-- Индекс: auth_user_groups_group_id_97559544
CREATE INDEX IF NOT EXISTS auth_user_groups_group_id_97559544 ON auth_user_groups (
    "group_id"
);


-- Индекс: auth_user_groups_user_id_6a12ed8b
CREATE INDEX IF NOT EXISTS auth_user_groups_user_id_6a12ed8b ON auth_user_groups (
    "user_id"
);


-- Индекс: auth_user_groups_user_id_group_id_94350c0c_uniq
CREATE UNIQUE INDEX IF NOT EXISTS auth_user_groups_user_id_group_id_94350c0c_uniq ON auth_user_groups (
    "user_id",
    "group_id"
);


-- Индекс: auth_user_user_permissions_permission_id_1fbb5f2c
CREATE INDEX IF NOT EXISTS auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions (
    "permission_id"
);


-- Индекс: auth_user_user_permissions_user_id_a95ead1b
CREATE INDEX IF NOT EXISTS auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions (
    "user_id"
);


-- Индекс: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
CREATE UNIQUE INDEX IF NOT EXISTS auth_user_user_permissions_user_id_permission_id_14a6b632_uniq ON auth_user_user_permissions (
    "user_id",
    "permission_id"
);


-- Индекс: django_admin_log_content_type_id_c4bce8eb
CREATE INDEX IF NOT EXISTS django_admin_log_content_type_id_c4bce8eb ON django_admin_log (
    "content_type_id"
);


-- Индекс: django_admin_log_user_id_c564eba6
CREATE INDEX IF NOT EXISTS django_admin_log_user_id_c564eba6 ON django_admin_log (
    "user_id"
);


-- Индекс: django_content_type_app_label_model_76bd3d3b_uniq
CREATE UNIQUE INDEX IF NOT EXISTS django_content_type_app_label_model_76bd3d3b_uniq ON django_content_type (
    "app_label",
    "model"
);


-- Индекс: django_session_expire_date_a5c62663
CREATE INDEX IF NOT EXISTS django_session_expire_date_a5c62663 ON django_session (
    "expire_date"
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
