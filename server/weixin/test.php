<?php
/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/20,0020
 * Time: 21:15
 */
$dbhandle = sqlite_open('sqlitedb.db');
$query = sqlite_query($dbhandle, "SELECT COUNT(openid) FROM users WHERE openid=='$id'", SQLITE_ASSOC, $query_error);
sqlite_close($dbhandle);
$result = sqlite_fetch_all($query);
echo var_dump($result);

?>