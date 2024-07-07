--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.3 в Вс июл 7 20:36:11 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: auth_group
DROP TABLE IF EXISTS auth_group;

CREATE TABLE IF NOT EXISTS auth_group (
    id   INTEGER       NOT NULL
                       PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (150) NOT NULL
                       UNIQUE
);

INSERT INTO auth_group (
                           id,
                           name
                       )
                       VALUES (
                           1,
                           'admin'
                       );

INSERT INTO auth_group (
                           id,
                           name
                       )
                       VALUES (
                           2,
                           'headAdmin'
                       );

INSERT INTO auth_group (
                           id,
                           name
                       )
                       VALUES (
                           3,
                           'worker'
                       );

INSERT INTO auth_group (
                           id,
                           name
                       )
                       VALUES (
                           4,
                           'Section_Chief'
                       );

INSERT INTO auth_group (
                           id,
                           name
                       )
                       VALUES (
                           5,
                           'HR'
                       );


-- Таблица: auth_group_permissions
DROP TABLE IF EXISTS auth_group_permissions;

CREATE TABLE IF NOT EXISTS auth_group_permissions (
    id            INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    group_id      INTEGER NOT NULL
                          REFERENCES auth_group (id) DEFERRABLE INITIALLY DEFERRED,
    permission_id INTEGER NOT NULL
                          REFERENCES auth_permission (id) DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       169,
                                       5,
                                       96
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       170,
                                       5,
                                       97
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       171,
                                       5,
                                       98
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       172,
                                       5,
                                       28
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       173,
                                       5,
                                       91
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       174,
                                       5,
                                       92
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       175,
                                       5,
                                       93
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       176,
                                       5,
                                       94
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       177,
                                       5,
                                       95
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       178,
                                       4,
                                       75
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       179,
                                       4,
                                       86
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       180,
                                       4,
                                       87
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       181,
                                       4,
                                       88
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       182,
                                       4,
                                       89
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       183,
                                       4,
                                       90
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       184,
                                       1,
                                       1
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       185,
                                       1,
                                       2
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       186,
                                       1,
                                       3
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       187,
                                       1,
                                       4
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       188,
                                       1,
                                       5
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       189,
                                       1,
                                       6
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       190,
                                       1,
                                       7
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       191,
                                       1,
                                       8
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       192,
                                       1,
                                       9
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       193,
                                       1,
                                       10
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       194,
                                       1,
                                       11
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       195,
                                       1,
                                       12
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       196,
                                       1,
                                       13
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       197,
                                       1,
                                       14
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       198,
                                       1,
                                       15
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       199,
                                       1,
                                       16
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       200,
                                       1,
                                       17
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       201,
                                       1,
                                       18
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       202,
                                       1,
                                       19
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       203,
                                       1,
                                       20
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       204,
                                       1,
                                       21
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       205,
                                       1,
                                       22
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       206,
                                       1,
                                       23
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       207,
                                       1,
                                       24
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       208,
                                       1,
                                       25
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       209,
                                       1,
                                       26
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       210,
                                       1,
                                       27
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       211,
                                       1,
                                       28
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       212,
                                       1,
                                       29
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       213,
                                       1,
                                       30
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       214,
                                       1,
                                       31
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       215,
                                       1,
                                       32
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       216,
                                       1,
                                       33
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       217,
                                       1,
                                       34
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       218,
                                       1,
                                       35
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       219,
                                       1,
                                       36
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       220,
                                       1,
                                       37
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       221,
                                       1,
                                       38
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       222,
                                       1,
                                       39
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       223,
                                       1,
                                       40
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       224,
                                       1,
                                       41
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       225,
                                       1,
                                       42
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       226,
                                       1,
                                       43
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       227,
                                       1,
                                       44
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       228,
                                       1,
                                       75
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       229,
                                       1,
                                       76
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       230,
                                       1,
                                       77
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       231,
                                       1,
                                       78
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       232,
                                       1,
                                       79
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       233,
                                       1,
                                       80
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       234,
                                       1,
                                       81
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       235,
                                       1,
                                       82
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       236,
                                       1,
                                       83
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       237,
                                       1,
                                       84
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       238,
                                       1,
                                       85
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       239,
                                       1,
                                       86
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       240,
                                       1,
                                       87
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       241,
                                       1,
                                       88
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       242,
                                       1,
                                       89
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       243,
                                       1,
                                       90
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       244,
                                       1,
                                       91
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       245,
                                       1,
                                       92
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       246,
                                       1,
                                       93
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       247,
                                       1,
                                       94
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       248,
                                       1,
                                       95
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       249,
                                       1,
                                       96
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       250,
                                       1,
                                       97
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       251,
                                       1,
                                       98
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       252,
                                       1,
                                       99
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       253,
                                       1,
                                       100
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       254,
                                       1,
                                       101
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       255,
                                       1,
                                       102
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       256,
                                       1,
                                       103
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       257,
                                       1,
                                       104
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       258,
                                       2,
                                       75
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       259,
                                       2,
                                       76
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       260,
                                       2,
                                       77
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       261,
                                       2,
                                       78
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       262,
                                       2,
                                       79
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       263,
                                       2,
                                       80
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       264,
                                       2,
                                       81
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       265,
                                       2,
                                       82
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       266,
                                       2,
                                       83
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       267,
                                       2,
                                       84
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       268,
                                       2,
                                       85
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       269,
                                       2,
                                       86
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       270,
                                       2,
                                       87
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       271,
                                       2,
                                       88
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       272,
                                       2,
                                       89
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       273,
                                       2,
                                       90
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       274,
                                       2,
                                       91
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       275,
                                       2,
                                       92
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       276,
                                       2,
                                       93
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       277,
                                       2,
                                       94
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       278,
                                       2,
                                       95
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       279,
                                       2,
                                       96
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       280,
                                       2,
                                       97
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       281,
                                       2,
                                       98
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       282,
                                       2,
                                       99
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       283,
                                       2,
                                       100
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       284,
                                       2,
                                       101
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       285,
                                       2,
                                       102
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       286,
                                       2,
                                       103
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       287,
                                       2,
                                       104
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       288,
                                       3,
                                       88
                                   );

INSERT INTO auth_group_permissions (
                                       id,
                                       group_id,
                                       permission_id
                                   )
                                   VALUES (
                                       289,
                                       3,
                                       75
                                   );


-- Таблица: auth_permission
DROP TABLE IF EXISTS auth_permission;

CREATE TABLE IF NOT EXISTS auth_permission (
    id              INTEGER       NOT NULL
                                  PRIMARY KEY AUTOINCREMENT,
    content_type_id INTEGER       NOT NULL
                                  REFERENCES django_content_type (id) DEFERRABLE INITIALLY DEFERRED,
    codename        VARCHAR (100) NOT NULL,
    name            VARCHAR (255) NOT NULL
);

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                1,
                                1,
                                'add_logentry',
                                'Can add log entry'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                2,
                                1,
                                'change_logentry',
                                'Can change log entry'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                3,
                                1,
                                'delete_logentry',
                                'Can delete log entry'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                4,
                                1,
                                'view_logentry',
                                'Can view log entry'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                5,
                                2,
                                'add_permission',
                                'Can add permission'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                6,
                                2,
                                'change_permission',
                                'Can change permission'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                7,
                                2,
                                'delete_permission',
                                'Can delete permission'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                8,
                                2,
                                'view_permission',
                                'Can view permission'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                9,
                                3,
                                'add_group',
                                'Can add group'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                10,
                                3,
                                'change_group',
                                'Can change group'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                11,
                                3,
                                'delete_group',
                                'Can delete group'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                12,
                                3,
                                'view_group',
                                'Can view group'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                13,
                                4,
                                'add_contenttype',
                                'Can add content type'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                14,
                                4,
                                'change_contenttype',
                                'Can change content type'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                15,
                                4,
                                'delete_contenttype',
                                'Can delete content type'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                16,
                                4,
                                'view_contenttype',
                                'Can view content type'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                17,
                                5,
                                'add_session',
                                'Can add session'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                18,
                                5,
                                'change_session',
                                'Can change session'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                19,
                                5,
                                'delete_session',
                                'Can delete session'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                20,
                                5,
                                'view_session',
                                'Can view session'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                21,
                                6,
                                'add_positions',
                                'Can add Должность'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                22,
                                6,
                                'change_positions',
                                'Can change Должность'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                23,
                                6,
                                'delete_positions',
                                'Can delete Должность'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                24,
                                6,
                                'view_positions',
                                'Can view Должность'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                25,
                                7,
                                'add_user',
                                'Can add пользователя'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                26,
                                7,
                                'change_user',
                                'Can change пользователя'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                27,
                                7,
                                'delete_user',
                                'Can delete пользователя'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                28,
                                7,
                                'view_user',
                                'Can view пользователя'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                29,
                                8,
                                'add_specifications',
                                'Can add Спецификация инцидентов'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                30,
                                8,
                                'change_specifications',
                                'Can change Спецификация инцидентов'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                31,
                                8,
                                'delete_specifications',
                                'Can delete Спецификация инцидентов'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                32,
                                8,
                                'view_specifications',
                                'Can view Спецификация инцидентов'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                33,
                                9,
                                'add_status',
                                'Can add Статус происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                34,
                                9,
                                'change_status',
                                'Can change Статус происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                35,
                                9,
                                'delete_status',
                                'Can delete Статус происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                36,
                                9,
                                'view_status',
                                'Can view Статус происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                37,
                                10,
                                'add_incidents',
                                'Can add инцидент'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                38,
                                10,
                                'change_incidents',
                                'Can change инцидент'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                39,
                                10,
                                'delete_incidents',
                                'Can delete инцидент'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                40,
                                10,
                                'view_incidents',
                                'Can view инцидент'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                41,
                                11,
                                'add_subdivisions',
                                'Can add Подразделение'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                42,
                                11,
                                'change_subdivisions',
                                'Can change Подразделение'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                43,
                                11,
                                'delete_subdivisions',
                                'Can delete Подразделение'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                44,
                                11,
                                'view_subdivisions',
                                'Can view Подразделение'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                75,
                                10,
                                'Incidents.incidents_add',
                                'Добавление происшествий'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                76,
                                8,
                                'Incidents.specification_add',
                                'Добавление спецификации происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                77,
                                8,
                                'Incidents.specification_change',
                                'Изменение спецификации происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                78,
                                8,
                                'Incidents.specification_delete',
                                'Удаление спецификации происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                79,
                                8,
                                'Incidents.specification_id',
                                'Просмотр спецификации происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                80,
                                8,
                                'Incidents.specification_all',
                                'Просмотр всех спецификаций в таблице'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                81,
                                9,
                                'Incidents.status_add',
                                'Добавление статуса происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                82,
                                9,
                                'Incidents.status_change',
                                'Изменение статуса происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                83,
                                9,
                                'Incidents.status_delete',
                                'Удаление статуса происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                84,
                                9,
                                'Incidents.status_id',
                                'Просмотр статуса происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                85,
                                9,
                                'Incidents.status_all',
                                'Просмотр всех статусов в таблице'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                86,
                                10,
                                'Incidents.incidents_change',
                                'Изменение происшествий'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                87,
                                10,
                                'Incidents.incidents_delete',
                                'Удаление происшествий'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                88,
                                10,
                                'Incidents.incidents_id',
                                'Просмотр происшествия'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                89,
                                10,
                                'Incidents.incidents_map',
                                'Просмотр всех происшествий на карте'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                90,
                                10,
                                'Incidents.incidents_all',
                                'Просмотр всех происшествий в таблице'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                91,
                                6,
                                'users.position_add',
                                'Добавление должностей'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                92,
                                6,
                                'users.position_change',
                                'Изменение должностей'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                93,
                                6,
                                'users.position_delete',
                                'Удаление должностей'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                94,
                                6,
                                'users.position_id',
                                'Просмотр должности'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                95,
                                6,
                                'users.position_all',
                                'Просмотр всех должностей в таблице'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                96,
                                7,
                                'users.user_id',
                                'Просмотр пользователей'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                97,
                                7,
                                'users.user_delete',
                                'Удаление пользователей'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                98,
                                7,
                                'users.user_all',
                                'Просмотр всех пользователей в таблице'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                99,
                                11,
                                'Subdivisions.subdivision_add',
                                'Добавление подразделения'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                100,
                                11,
                                'Subdivisions.subdivision_change',
                                'Изменение подразделения'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                101,
                                11,
                                'Subdivisions.subdivision_delete',
                                'Удаление подразделения'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                102,
                                11,
                                'Subdivisions.subdivision_id',
                                'Просмотр подразделения'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                103,
                                11,
                                'Subdivisions.subdivision_map',
                                'Просмотр всех подразделений на карте'
                            );

INSERT INTO auth_permission (
                                id,
                                content_type_id,
                                codename,
                                name
                            )
                            VALUES (
                                104,
                                11,
                                'Subdivisions.subdivision_all',
                                'Просмотр всех подразделений в таблице'
                            );


-- Таблица: Incidents_incidents
DROP TABLE IF EXISTS Incidents_incidents;

CREATE TABLE IF NOT EXISTS Incidents_incidents (
    id                  INTEGER       NOT NULL
                                      PRIMARY KEY AUTOINCREMENT,
    address             VARCHAR (255) NOT NULL,
    description         VARCHAR (255) NOT NULL,
    latitude            REAL          NOT NULL,
    longitude           REAL          NOT NULL,
    taken_measures      VARCHAR (255),
    specification_id    BIGINT        NOT NULL
                                      REFERENCES Incidents_specifications (id) DEFERRABLE INITIALLY DEFERRED,
    user_create_id      BIGINT        NOT NULL
                                      REFERENCES users_user (id) DEFERRABLE INITIALLY DEFERRED,
    user_responsible_id BIGINT        NOT NULL
                                      REFERENCES users_user (id) DEFERRABLE INITIALLY DEFERRED,
    status_id           BIGINT        NOT NULL
                                      REFERENCES Incidents_status (id) DEFERRABLE INITIALLY DEFERRED,
    time_end            DATETIME,
    time_start          DATETIME,
    complete            BOOL,
    time_create         DATETIME      NOT NULL
);

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    47,
                                    'г Москва, Костомаровская наб, д 29 стр 3',
                                    'Обрыв линии связи',
                                    55.75092196489011,
                                    37.66937255859376,
                                    NULL,
                                    2,
                                    4,
                                    1,
                                    3,
                                    NULL,
                                    NULL,
                                    0,
                                    '2024-05-08 18:58:57.012182'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    48,
                                    'г Москва, ул Краснопрудная, д 3/5 стр 6',
                                    'Дефекты путей. Путь - 1а.',
                                    55.7806832500177,
                                    37.65689492225648,
                                    NULL,
                                    3,
                                    2,
                                    1,
                                    3,
                                    NULL,
                                    NULL,
                                    0,
                                    '2024-05-08 18:59:51.167461'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    49,
                                    'г Москва, Комсомольская пл, д 3',
                                    'Прорыв водопровода. 1 этаж.',
                                    55.77636423733031,
                                    37.65539288520814,
                                    NULL,
                                    1,
                                    9,
                                    1,
                                    3,
                                    NULL,
                                    NULL,
                                    0,
                                    '2024-05-08 19:00:35.938293'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    50,
                                    'г Москва, 5-й Красносельский пер, д 17 стр 2',
                                    'Обрушение путей. Просадка грунта.
Путь - 51.',
                                    55.78572993900495,
                                    37.65430390834809,
                                    'Выезд экстренной службы.',
                                    3,
                                    2,
                                    1,
                                    1,
                                    NULL,
                                    '2024-05-08 20:21:34.145554',
                                    0,
                                    '2024-05-08 19:01:31.078742'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    51,
                                    'Москва, 51-км',
                                    'Обрушение моста запасной жд.',
                                    55.49357924953389,
                                    37.84652709960938,
                                    NULL,
                                    2,
                                    2,
                                    1,
                                    3,
                                    NULL,
                                    NULL,
                                    0,
                                    '2024-05-08 19:02:54.799477'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    52,
                                    'г Москва, ул Верхняя Красносельская, д 10А стр 4',
                                    'Нарушена работа стрелки перевода',
                                    55.78231829197123,
                                    37.65587568283082,
                                    NULL,
                                    3,
                                    5,
                                    1,
                                    3,
                                    NULL,
                                    NULL,
                                    0,
                                    '2024-05-08 19:24:39.926760'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    53,
                                    'Москва, 64-км',
                                    'Износ несущих конструкций моста.',
                                    55.23627664254681,
                                    37.48929977416993,
                                    'Выезд экстренной службы участка. Ремонт изношенных конструкций.',
                                    3,
                                    1,
                                    1,
                                    2,
                                    '2024-05-08 20:14:05.377012',
                                    '2024-05-08 20:10:45.087793',
                                    1,
                                    '2024-05-08 20:07:23.720725'
                                );

INSERT INTO Incidents_incidents (
                                    id,
                                    address,
                                    description,
                                    latitude,
                                    longitude,
                                    taken_measures,
                                    specification_id,
                                    user_create_id,
                                    user_responsible_id,
                                    status_id,
                                    time_end,
                                    time_start,
                                    complete,
                                    time_create
                                )
                                VALUES (
                                    54,
                                    'Москва №1',
                                    'Какой-то дефект',
                                    56.1484583354556,
                                    37.94104278087617,
                                    'Меры №1',
                                    2,
                                    1,
                                    1,
                                    2,
                                    '2024-06-10 18:56:32.832020',
                                    '2024-06-10 18:56:15.664147',
                                    1,
                                    '2024-06-10 18:56:00.858026'
                                );


-- Таблица: Incidents_specifications
DROP TABLE IF EXISTS Incidents_specifications;

CREATE TABLE IF NOT EXISTS Incidents_specifications (
    id      INTEGER       NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    pattern VARCHAR (100) NOT NULL,
    color   VARCHAR (20)  NOT NULL
);

INSERT INTO Incidents_specifications (
                                         id,
                                         pattern,
                                         color
                                     )
                                     VALUES (
                                         1,
                                         'Происшествий низкой опасности',
                                         'green'
                                     );

INSERT INTO Incidents_specifications (
                                         id,
                                         pattern,
                                         color
                                     )
                                     VALUES (
                                         2,
                                         'Происшествий средней опасности',
                                         'orange'
                                     );

INSERT INTO Incidents_specifications (
                                         id,
                                         pattern,
                                         color
                                     )
                                     VALUES (
                                         3,
                                         'Происшествий высокой опасности',
                                         'red'
                                     );


-- Таблица: Incidents_status
DROP TABLE IF EXISTS Incidents_status;

CREATE TABLE IF NOT EXISTS Incidents_status (
    id          INTEGER       NOT NULL
                              PRIMARY KEY AUTOINCREMENT,
    status      VARCHAR (100) NOT NULL,
    description VARCHAR (100) NOT NULL
);

INSERT INTO Incidents_status (
                                 id,
                                 status,
                                 description
                             )
                             VALUES (
                                 1,
                                 'В работе',
                                 'Выдвинуты меры по ликвидации происшествия'
                             );

INSERT INTO Incidents_status (
                                 id,
                                 status,
                                 description
                             )
                             VALUES (
                                 2,
                                 'Ликвидировано',
                                 'Происшествие было ликвидировано'
                             );

INSERT INTO Incidents_status (
                                 id,
                                 status,
                                 description
                             )
                             VALUES (
                                 3,
                                 'Обнаружено',
                                 'Происшествие обнаружено и создана заявка'
                             );


-- Таблица: Subdivisions_subdivisions
DROP TABLE IF EXISTS Subdivisions_subdivisions;

CREATE TABLE IF NOT EXISTS Subdivisions_subdivisions (
    id           INTEGER       NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    address      VARCHAR (250) NOT NULL,
    abbreviation VARCHAR (10)  NOT NULL,
    description  VARCHAR (250) NOT NULL,
    latitude     REAL          NOT NULL,
    longitude    REAL          NOT NULL
);

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          1,
                                          'г Москва, ул Бориса Жигулёнкова, д 2',
                                          'ЦСС',
                                          'Центральная станция связи',
                                          55.77419147765099,
                                          37.73260116227903
                                      );

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          2,
                                          'г Москва, Индустриальный пер, д 9 стр 7',
                                          'ЭЧ',
                                          'Службы электрификации и электроснабжения',
                                          55.78537703089696,
                                          37.64328002929688
                                      );

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          3,
                                          'г Москва, пр-кт Мира, д 94 стр 1',
                                          'ПЧ',
                                          'Службы пути и сооружений',
                                          55.79711260508441,
                                          37.63538360595704
                                      );

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          4,
                                          'г Москва',
                                          'НГЧ',
                                          'Служба гражданских сооружений',
                                          55.68563661125317,
                                          37.65701293945313
                                      );

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          5,
                                          'г Москва, Мжд Казанское 4-й км, стр 5',
                                          'СЦБ',
                                          'Службы автоматики и телемеханики',
                                          55.79155409243336,
                                          37.64602661132813
                                      );

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          6,
                                          'г Москва, ул Старая Басманная, д 30/1 стр 2',
                                          'ПЧУ',
                                          'Начальник участка',
                                          55.76834642885029,
                                          37.66834259033204
                                      );

INSERT INTO Subdivisions_subdivisions (
                                          id,
                                          address,
                                          abbreviation,
                                          description,
                                          latitude,
                                          longitude
                                      )
                                      VALUES (
                                          7,
                                          'г Москва, ул Краснопрудная, д 3/5 стр 5',
                                          'ЭС',
                                          'Экстренная служба участка',
                                          55.77981683448109,
                                          37.65769958496094
                                      );


-- Таблица: users_positions
DROP TABLE IF EXISTS users_positions;

CREATE TABLE IF NOT EXISTS users_positions (
    id        INTEGER       NOT NULL
                            PRIMARY KEY AUTOINCREMENT,
    positions VARCHAR (255) NOT NULL
);

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                2,
                                'Инженер-связист'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                3,
                                'Дежурный стрелочных постов'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                4,
                                'Дежурный путевого хозяйства'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                5,
                                'Инженер-электрик путей сообщения'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                7,
                                'Начальник участка'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                8,
                                'Инженер'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                10,
                                'Нет должности'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                14,
                                'Сотрудник управления персоналом'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                15,
                                'Работник экстренной службы участка'
                            );

INSERT INTO users_positions (
                                id,
                                positions
                            )
                            VALUES (
                                16,
                                'Начальник экстренной службы участка'
                            );


-- Таблица: users_user
DROP TABLE IF EXISTS users_user;

CREATE TABLE IF NOT EXISTS users_user (
    id             INTEGER       NOT NULL
                                 PRIMARY KEY AUTOINCREMENT,
    email          VARCHAR (255) NOT NULL
                                 UNIQUE,
    name           VARCHAR (50)  NOT NULL,
    surname        VARCHAR (50)  NOT NULL,
    lastname       VARCHAR (50)  NOT NULL,
    fullname       VARCHAR (255) NOT NULL,
    subdivision_id BIGINT        NOT NULL
                                 REFERENCES Subdivisions_subdivisions (id) DEFERRABLE INITIALLY DEFERRED,
    password       VARCHAR (128) NOT NULL,
    last_login     DATETIME,
    is_superuser   BOOL          NOT NULL,
    is_staff       BOOL          NOT NULL,
    position_id    BIGINT        NOT NULL
                                 REFERENCES users_positions (id) DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           1,
                           'B_A_M2000@mail.ru',
                           'Антон',
                           'Богушевич',
                           'Максимович',
                           'Богушевич Антон Максимович',
                           6,
                           'pbkdf2_sha256$600000$UARY3KFqd53yzMZ1EfZQGv$TIFRlHhLI1E/mAUEK3Et5zgoIOWHS5tKyFD0/wEiwS0=',
                           '2024-06-10 15:54:10.488915',
                           1,
                           1,
                           7
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           2,
                           'headAdmin@mail.ru',
                           'Аделина',
                           'Касаткина',
                           'Сергеевна',
                           'qwerty qwerty qwerty',
                           3,
                           'pbkdf2_sha256$600000$aPgUUPc7sNirm5krDgQ4Hq$RVXwFj3EN5s0iBwDZQ87kUzeDnBuEg1vOZzar00Xri4=',
                           '2024-04-21 12:21:40.290770',
                           1,
                           1,
                           4
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           3,
                           'HR@mail.ru',
                           'София',
                           'Гаврилова',
                           'Вадимовна',
                           'Hr HR HR',
                           1,
                           'pbkdf2_sha256$600000$mesgRHlvYP4SwJfDw99fpB$q6o77EhTsFhTDRsF/t4IaiQLRNzvLHCsgHpm7vjgD0c=',
                           '2024-05-08 18:48:39.511855',
                           0,
                           0,
                           14
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           4,
                           'Section_chief@mail.ru',
                           'Владислав',
                           'Романов',
                           'Игоревич',
                           'Section_Chief Section_Chief Section_Chief',
                           1,
                           'pbkdf2_sha256$600000$TMaj9qWx3r7YHXRDtFfxpZ$WSOPDVku8gAvWAm4K5D4wLUBIVF4RtLtHaqWv1fgeyM=',
                           '2024-05-06 15:46:44.729515',
                           0,
                           0,
                           2
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           5,
                           'admin@mail.ru',
                           'Дмитрий',
                           'Седов',
                           'Романович',
                           'admin admin admin',
                           5,
                           'pbkdf2_sha256$600000$8oRHoD5mK8pmSJmJm6dsA9$HqJ7yVWi9I5sPN8XB76Z1c2GpcYcQT82jiULs5Wo6co=',
                           '2024-04-21 15:54:12.032358',
                           1,
                           1,
                           3
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           6,
                           'worker@mail.ru',
                           'Марсель',
                           'Поздняков',
                           'Артёмович',
                           'worker worker worker',
                           7,
                           'pbkdf2_sha256$600000$Jxj5jrPKDt88Eq0hAVIBmw$Fk5k8ZqiWoTMpWjV3hZewvGlRCL5iMx9dJamnpVwo0E=',
                           '2024-07-07 17:21:36.104887',
                           0,
                           0,
                           15
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           8,
                           'test5@mail.ru',
                           'Родион',
                           'Уткин',
                           'Артурович',
                           'Нет полного имени',
                           2,
                           'pbkdf2_sha256$600000$zZAcXv4nRldTYAMxHJulGl$dk3UBvL2nfaHLRNoApkqkIvl0AH2Xmkrc5sh/smGSOM=',
                           NULL,
                           0,
                           0,
                           5
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           9,
                           'NGCH@mail.ru',
                           'Иннокентий',
                           'Тимофеев',
                           'Артемович',
                           'Нет полного имени',
                           4,
                           'pbkdf2_sha256$600000$BIElGwGIOgfIus0nZIx6E4$ffZaUV/vZSblNSUZgQgRNZmCEsV0kBZExQFkjrrTdRM=',
                           NULL,
                           0,
                           0,
                           15
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           10,
                           'testChief@mail.ru',
                           'Игорь',
                           'Дьячков',
                           'Филатович',
                           'Нет полного имени',
                           1,
                           'pbkdf2_sha256$600000$EKQxKv9geODGrkgSh9TuZC$84hHpsRNFR/Igv8MyrbL/T2qvhDR/yGoXTrBmHCp4cY=',
                           '2024-05-08 18:47:24.110318',
                           0,
                           0,
                           10
                       );

INSERT INTO users_user (
                           id,
                           email,
                           name,
                           surname,
                           lastname,
                           fullname,
                           subdivision_id,
                           password,
                           last_login,
                           is_superuser,
                           is_staff,
                           position_id
                       )
                       VALUES (
                           11,
                           'NES@mail.ru',
                           'Эрик',
                           'Костин',
                           'Дмитрьевич',
                           'Нет полного имени',
                           1,
                           'pbkdf2_sha256$600000$J8MPLQnaQB8jJ4y2u8lulx$/t2ftTcbymue588B0Qgvp30dr9iTcjAM6Vh+tc2E3iQ=',
                           '2024-05-08 18:48:06.889990',
                           0,
                           0,
                           10
                       );


-- Таблица: users_user_groups
DROP TABLE IF EXISTS users_user_groups;

CREATE TABLE IF NOT EXISTS users_user_groups (
    id       INTEGER NOT NULL
                     PRIMARY KEY AUTOINCREMENT,
    user_id  BIGINT  NOT NULL
                     REFERENCES users_user (id) DEFERRABLE INITIALLY DEFERRED,
    group_id INTEGER NOT NULL
                     REFERENCES auth_group (id) DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  8,
                                  3,
                                  5
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  9,
                                  4,
                                  4
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  12,
                                  6,
                                  3
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  13,
                                  8,
                                  3
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  14,
                                  2,
                                  3
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  15,
                                  5,
                                  3
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  16,
                                  1,
                                  4
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  17,
                                  9,
                                  3
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  18,
                                  1,
                                  1
                              );

INSERT INTO users_user_groups (
                                  id,
                                  user_id,
                                  group_id
                              )
                              VALUES (
                                  19,
                                  10,
                                  4
                              );


-- Таблица: users_user_user_permissions
DROP TABLE IF EXISTS users_user_user_permissions;

CREATE TABLE IF NOT EXISTS users_user_user_permissions (
    id            INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    user_id       BIGINT  NOT NULL
                          REFERENCES users_user (id) DEFERRABLE INITIALLY DEFERRED,
    permission_id INTEGER NOT NULL
                          REFERENCES auth_permission (id) DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            2,
                                            8,
                                            88
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            3,
                                            1,
                                            1
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            4,
                                            1,
                                            2
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            5,
                                            1,
                                            3
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            6,
                                            1,
                                            4
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            7,
                                            1,
                                            5
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            8,
                                            1,
                                            6
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            9,
                                            1,
                                            7
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            10,
                                            1,
                                            8
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            11,
                                            1,
                                            9
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            12,
                                            1,
                                            10
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            13,
                                            1,
                                            11
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            14,
                                            1,
                                            12
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            15,
                                            1,
                                            13
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            16,
                                            1,
                                            14
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            17,
                                            1,
                                            15
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            18,
                                            1,
                                            16
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            19,
                                            1,
                                            17
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            20,
                                            1,
                                            18
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            21,
                                            1,
                                            19
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            22,
                                            1,
                                            20
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            23,
                                            1,
                                            21
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            24,
                                            1,
                                            22
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            25,
                                            1,
                                            23
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            26,
                                            1,
                                            24
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            27,
                                            1,
                                            25
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            28,
                                            1,
                                            26
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            29,
                                            1,
                                            27
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            30,
                                            1,
                                            28
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            31,
                                            1,
                                            29
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            32,
                                            1,
                                            30
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            33,
                                            1,
                                            31
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            34,
                                            1,
                                            32
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            35,
                                            1,
                                            33
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            36,
                                            1,
                                            34
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            37,
                                            1,
                                            35
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            38,
                                            1,
                                            36
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            39,
                                            1,
                                            37
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            40,
                                            1,
                                            38
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            41,
                                            1,
                                            39
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            42,
                                            1,
                                            40
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            43,
                                            1,
                                            41
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            44,
                                            1,
                                            42
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            45,
                                            1,
                                            43
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            46,
                                            1,
                                            44
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            47,
                                            1,
                                            75
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            48,
                                            1,
                                            76
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            49,
                                            1,
                                            77
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            50,
                                            1,
                                            78
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            51,
                                            1,
                                            79
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            52,
                                            1,
                                            80
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            53,
                                            1,
                                            81
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            54,
                                            1,
                                            82
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            55,
                                            1,
                                            83
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            56,
                                            1,
                                            84
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            57,
                                            1,
                                            85
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            58,
                                            1,
                                            86
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            59,
                                            1,
                                            87
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            60,
                                            1,
                                            88
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            61,
                                            1,
                                            89
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            62,
                                            1,
                                            90
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            63,
                                            1,
                                            91
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            64,
                                            1,
                                            92
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            65,
                                            1,
                                            93
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            66,
                                            1,
                                            94
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            67,
                                            1,
                                            95
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            68,
                                            1,
                                            96
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            69,
                                            1,
                                            97
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            70,
                                            1,
                                            98
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            71,
                                            1,
                                            99
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            72,
                                            1,
                                            100
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            73,
                                            1,
                                            101
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            74,
                                            1,
                                            102
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            75,
                                            1,
                                            103
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            76,
                                            1,
                                            104
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            77,
                                            11,
                                            88
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            78,
                                            11,
                                            89
                                        );

INSERT INTO users_user_user_permissions (
                                            id,
                                            user_id,
                                            permission_id
                                        )
                                        VALUES (
                                            79,
                                            11,
                                            90
                                        );


-- Индекс: auth_group_permissions_group_id_b120cbf9
DROP INDEX IF EXISTS auth_group_permissions_group_id_b120cbf9;

CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions (
    "group_id"
);


-- Индекс: auth_group_permissions_group_id_permission_id_0cd325b0_uniq
DROP INDEX IF EXISTS auth_group_permissions_group_id_permission_id_0cd325b0_uniq;

CREATE UNIQUE INDEX IF NOT EXISTS auth_group_permissions_group_id_permission_id_0cd325b0_uniq ON auth_group_permissions (
    "group_id",
    "permission_id"
);


-- Индекс: auth_group_permissions_permission_id_84c5c92e
DROP INDEX IF EXISTS auth_group_permissions_permission_id_84c5c92e;

CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions (
    "permission_id"
);


-- Индекс: auth_permission_content_type_id_2f476e4b
DROP INDEX IF EXISTS auth_permission_content_type_id_2f476e4b;

CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b ON auth_permission (
    "content_type_id"
);


-- Индекс: auth_permission_content_type_id_codename_01ab375a_uniq
DROP INDEX IF EXISTS auth_permission_content_type_id_codename_01ab375a_uniq;

CREATE UNIQUE INDEX IF NOT EXISTS auth_permission_content_type_id_codename_01ab375a_uniq ON auth_permission (
    "content_type_id",
    "codename"
);


-- Индекс: Incidents_incidents_specification_id_45db9ff5
DROP INDEX IF EXISTS Incidents_incidents_specification_id_45db9ff5;

CREATE INDEX IF NOT EXISTS Incidents_incidents_specification_id_45db9ff5 ON Incidents_incidents (
    "specification_id"
);


-- Индекс: Incidents_incidents_status_id_37b9af8a
DROP INDEX IF EXISTS Incidents_incidents_status_id_37b9af8a;

CREATE INDEX IF NOT EXISTS Incidents_incidents_status_id_37b9af8a ON Incidents_incidents (
    "status_id"
);


-- Индекс: Incidents_incidents_user_create_id_4009ce52
DROP INDEX IF EXISTS Incidents_incidents_user_create_id_4009ce52;

CREATE INDEX IF NOT EXISTS Incidents_incidents_user_create_id_4009ce52 ON Incidents_incidents (
    "user_create_id"
);


-- Индекс: Incidents_incidents_user_responsible_id_67e11215
DROP INDEX IF EXISTS Incidents_incidents_user_responsible_id_67e11215;

CREATE INDEX IF NOT EXISTS Incidents_incidents_user_responsible_id_67e11215 ON Incidents_incidents (
    "user_responsible_id"
);


-- Индекс: users_user_groups_group_id_9afc8d0e
DROP INDEX IF EXISTS users_user_groups_group_id_9afc8d0e;

CREATE INDEX IF NOT EXISTS users_user_groups_group_id_9afc8d0e ON users_user_groups (
    "group_id"
);


-- Индекс: users_user_groups_user_id_5f6f5a90
DROP INDEX IF EXISTS users_user_groups_user_id_5f6f5a90;

CREATE INDEX IF NOT EXISTS users_user_groups_user_id_5f6f5a90 ON users_user_groups (
    "user_id"
);


-- Индекс: users_user_groups_user_id_group_id_b88eab82_uniq
DROP INDEX IF EXISTS users_user_groups_user_id_group_id_b88eab82_uniq;

CREATE UNIQUE INDEX IF NOT EXISTS users_user_groups_user_id_group_id_b88eab82_uniq ON users_user_groups (
    "user_id",
    "group_id"
);


-- Индекс: users_user_position_id_747739f1
DROP INDEX IF EXISTS users_user_position_id_747739f1;

CREATE INDEX IF NOT EXISTS users_user_position_id_747739f1 ON users_user (
    "position_id"
);


-- Индекс: users_user_subdivision_id_d6eb66ce
DROP INDEX IF EXISTS users_user_subdivision_id_d6eb66ce;

CREATE INDEX IF NOT EXISTS users_user_subdivision_id_d6eb66ce ON users_user (
    "subdivision_id"
);


-- Индекс: users_user_user_permissions_permission_id_0b93982e
DROP INDEX IF EXISTS users_user_user_permissions_permission_id_0b93982e;

CREATE INDEX IF NOT EXISTS users_user_user_permissions_permission_id_0b93982e ON users_user_user_permissions (
    "permission_id"
);


-- Индекс: users_user_user_permissions_user_id_20aca447
DROP INDEX IF EXISTS users_user_user_permissions_user_id_20aca447;

CREATE INDEX IF NOT EXISTS users_user_user_permissions_user_id_20aca447 ON users_user_user_permissions (
    "user_id"
);


-- Индекс: users_user_user_permissions_user_id_permission_id_43338c45_uniq
DROP INDEX IF EXISTS users_user_user_permissions_user_id_permission_id_43338c45_uniq;

CREATE UNIQUE INDEX IF NOT EXISTS users_user_user_permissions_user_id_permission_id_43338c45_uniq ON users_user_user_permissions (
    "user_id",
    "permission_id"
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
