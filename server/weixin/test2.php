<?php

/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/10,0010
 * Time: 20:19
 */
class MyDB extends SQLiteDatabase
{
}

$db = new MyDB();
$db->__construct("mysqlitedb");
$db->exec('CREATE TABLE foo (bar STRING)');
$db->exec("INSERT INTO foo (bar) VALUES ('This is a test')");

$result = $db->query('SELECT bar FROM foo');
echo var_dump($result->fetchArray());
#echo $result->fetchArray()[0];
?>