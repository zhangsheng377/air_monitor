<?php
/**
 * Created by PhpStorm.
 * User: 43587
 * Date: 2017/2/10,0010
 * Time: 19:30
 */
$access_token = "";
$time_expires_in = -1;

update_access_token();

$sql_command = "SELECT name FROM sensor_names";
$query = mysqlite_do($sql_command);
$sensor_names = sqlite_fetch_all($query);
//echo $sensor_names[0][0] . "\t";

$sql_command = "SELECT * FROM users";
$query = mysqlite_do($sql_command);
$users_detail = sqlite_fetch_all($query);
foreach ($users_detail as $user_detail) {
    $openid = $user_detail["openid"];
    $device_id = $user_detail["device_id"];
    foreach ($sensor_names as $sensor_name) {
        $value_limit = $user_detail["$sensor_name[0]" . "_limit"];
        //echo "$value_limit\n";
        $sql_command = "SELECT sensor_$sensor_name[0] FROM devices WHERE device_id=='$device_id'";
        $query = mysqlite_do($sql_command);
        $result = sqlite_fetch_all($query);
        $sensor_id = $result[0]["sensor_$sensor_name[0]"];
        $value = yeelinkapi_read_lastvalue($device_id, $sensor_id);
        if ($sensor_name[0] == "PM2_5") {
            $sensor_truename = "PM2.5";
        } elseif ($sensor_name[0] == "HCHO") {
            $sensor_truename = "甲醛";
        } elseif ($sensor_name[0] == "MQ2") {
            $sensor_truename = "易燃气体";
        } else {
            $sensor_truename = $sensor_name[0];
        }
        if ($value > $value_limit) {
            echo "$value\n\r";
            echo "abs($value - $alertvalue)\n\r";
            echo "$time - $alerttime";
            $alertvalue = $user_detail["$sensor_name[0]_alertvalue"];
            if (abs($value - $alertvalue) > 0.1) {
                $time = time();
                $alerttime = $user_detail["$sensor_name[0]_alerttime"];
                if ($time - $alerttime > 60 * 30) {
                    $template = array(
                        'touser' => "$openid",
                        'template_id' => "NGh_7ivNtf_AhRY5TrKBNGBrV-HsqZveiTeMNKTSYYA",
                        'url' => "http://www.yeelink.net/devices/$device_id/#sensor_$sensor_id",
                        'data' => array(
                            'first' => array(
                                'value' => urlencode("您身边的 $sensor_truename 数值超过报警阈值！"),
                                'color' => "#743A3A"),
                            'second' => array(
                                'value' => urlencode("请注意身体健康！"),
                                'color' => "#743A3A"),
                            'third' => array(
                                'value' => urlencode("传感器数值："),
                                'color' => "#000000"),
                            'fourth' => array(
                                'value' => urlencode("$value"),
                                'color' => "#FF0000")));
                    $template_result = curl_request("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=$access_token", urldecode(json_encode($template)));
                    $template_json = json_decode($template_result, true);
                    if ($template_json["errmsg"] == "ok") {
                        $sql_command = "UPDATE users SET $sensor_name[0]_alertvalue = $value , $sensor_name[0]_alerttime = $time WHERE openid=='$openid'";
                        $is_exec = mysqlite_do($sql_command, $error);
                        if (!$is_exec) {
                            echo "$error";
                        }
                    }
                }
            }
        }
    }
}


function curl_request($durl, $data = null)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $durl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);//获取数据返回
    if (!empty($data)) {
        echo "curl_data:$data";
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    }
    $r = curl_exec($ch);
    //echo "url:$durl\nr:$r\n";
    curl_close($ch);
    return $r;
}

function update_access_token()
{
    global $access_token, $time_expires_in;
    $file_name = "access_token.dat";
    $file_read = fopen($file_name, "rb");
    $data_file = fscanf($file_read, "%s\t%d");
    fclose($file_read);
    //echo "up_0:" . $data_file[1] . "\n";
    if (time() < $data_file[1]) {
        $access_token = $data_file[0];
        $time_expires_in = $data_file[1];
    } else {
        $appid = "wx691945ff03ba6040";
        $appsecret = "1e22eb6471847adef6c330719a739773";
        $data = curl_request("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$appsecret");
        //echo "data:" . $data . "\n";
        $data_json = json_decode($data, true);
        $access_token = $data_json["access_token"];
        //echo "acc:" . $data_json["access_token"] . "\n";
        $time_expires_in = time() + $data_json["expires_in"] - 200;
        $file_write = fopen($file_name, "wb");
        fwrite($file_write, $access_token);
        fwrite($file_write, "\t");
        fwrite($file_write, $time_expires_in);
        fclose($file_write);
    }
}


function mysqlite_do($sql_command, &$error = null)
{
    $dbhandle = sqlite_open('sqlitedb.db');
    if (empty($error)) {
        $result = sqlite_query($dbhandle, "$sql_command");
    } else {
        $result = sqlite_exec($dbhandle, "$sql_command", $error);
    }
    sqlite_close($dbhandle);
    return $result;
}

function yeelinkapi_read_lastvalue($device_id, $sensor_id)
{
    $durl = "http://api.yeelink.net/v1.0/device/$device_id/sensor/$sensor_id/datapoints";
    $data = curl_request($durl);
    $data_json = json_decode($data, true);
    return $data_json["value"];
}

?>