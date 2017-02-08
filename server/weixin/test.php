<?php
/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/9,0009
 * Time: 01:17
 */
$device_id = 353097;
$sensor_id = 397985;
$durl = "http://api.yeelink.net/v1.0/device/$device_id/sensor/$sensor_id/datapoints";
$data = file_get_contents($durl);
$data_json = json_decode($data);
$contentStr = 'value : ' . $data_json->value;
echo $contentStr

?>