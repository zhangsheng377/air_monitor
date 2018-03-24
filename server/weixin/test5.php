<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php echo 'Hello World'; ?> 

<?php
echo 'hello';
$dbhandle = new SQLite3('sqlitedb.db');
if($dbhandle){
echo 'success';
}else{
echo 'fail';
}

//$query = $dbhandle->query("SELECT name FROM sensor_names") or die($dbhandle->lastErrorMsg());
 //$dbhandle->close();
 $sql_command="SELECT name FROM sensor_names";
$dbhandle = new SQLite3('sqlitedb.db');
        if (empty($error)) {
            $result = $dbhandle->query("$sql_command");
        } else {
            $result = $dbhandle->exec("$sql_command");
        }
        //$dbhandle->close();
        //return $result;
        $query=$result;

 while ($entry=$query->fetchArray()){
     $name = $entry['name'];
     echo var_dump($name);
 }

 echo rand(0,200)*1.0/1000.0;

//$result = $query->fetchArray();
//echo $result[0];
//while($result = $query->fetchArray()){
//        echo var_dump($result);
//}


?>

 </body>
</html>
