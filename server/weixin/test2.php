<?php
/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/10,0010
 * Time: 20:19
 */

echo "hello\n";

$data_return=ini_set('safe_mode','Off');
$data_return_0 = ignore_user_abort(true);
$data_return_1 = ini_set('max_execution_time', '0');
$data_return_2 = set_time_limit(0);
$file_write = fopen("data_return.dat", "wb");
fwrite($file_write, $data_return);
fwrite($file_write, "\n");
fwrite($file_write, $data_return_0);
fwrite($file_write, "\n");
fwrite($file_write, $data_return_1);
fwrite($file_write, "\n");
fwrite($file_write, $data_return_2);
fclose($file_write);

?>