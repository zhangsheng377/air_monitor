<?php

/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/10,0010
 * Time: 20:19
 */
if ($db = sqlite_open('sqlitedb.db', 0666, $sqliteerror)) {
    sqlite_query($db, "CREATE TABLE users ([openid] TEXT PRIMARY KEY NOT NULL,[device_id] TEXT NOT NULL DEFAULT 354298,[PM2.5_limit] DOUBLE NOT NULL DEFAULT 70.0,[CO_limit] DOUBLE NOT NULL DEFAULT 120.0,[SO2_limit] DOUBLE NOT NULL DEFAULT 40.0,[O3_limit] DOUBLE NOT NULL DEFAULT 99999.0)");
}

?>