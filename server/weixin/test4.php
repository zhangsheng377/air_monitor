<?php
/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/20,0020
 * Time: 21:15
 */
$dbhandle = new SQLite3('sqlitedb.db');
$query = $dbhandle->query("SELECT * FROM users");
$dbhandle->close();
while($result = $query->fetchArray()){ 
	echo var_dump($result);
}

?>
