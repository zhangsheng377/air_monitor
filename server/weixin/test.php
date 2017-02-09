<?php
/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/9,0009
 * Time: 01:17
 */

$file_name="access_token.dat";
$file=fopen($file_name,"wb");
fwrite($file,"sfdsf");
fwrite($file,"\t");
fwrite($file,123);
fclose($file);

$access_token = "";
$time_expires_in = -1;
$file_read=fopen($file_name,"rb");
$data=fscanf($file_read,"%s\t%d");
fclose($file_read);
print $data[0];
print $data[1]+1;

?>