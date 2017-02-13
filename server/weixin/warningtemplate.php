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

$device_id = 354298;
$sensor_id = 400111;
$durl = "http://api.yeelink.net/v1.0/device/$device_id/sensor/$sensor_id/datapoints";
$data = curl_request($durl);
$data_json = json_decode($data, true);
$value = $data_json["value"];

if ($value > 25) {
    $file_read = fopen("template_time.dat", "rb");
    $time_read = fscanf($file_read, "%d");
    fclose($file_read);
    if (time() - $time_read[0] > 60 * 30) {
        $user_openids = array("owYXAwaD036go9d6b3ELlyFMjjD0", "owYXAwfBY0hM3y_UM9dg9RyYntoU", "owYXAwYDA_hUSYTveYUR1jO0WaPQ", "owYXAwd6NXwAbjtI6Fj3xqDh2Bss", "owYXAwde8zDF3cATEzimiT7qjVjA");
        foreach ($user_openids as $openid) {
            $template = array('touser' => "$openid", 'template_id' => "Oh5bDFWIIdg8acICj639FGPeLNMNxP0X68uWykjZLuM", 'url' => "http://github.com/zhangsheng377", 'data' => array('first' => array('value' => urlencode("SO2传感器报警！"), 'color' => "#743A3A"), 'second' => array('value' => urlencode("$value"), 'color' => "#FF0000")));
            $data_template = curl_request("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=$access_token", urldecode(json_encode($template)));
        }
        $time_old = time();
        $file_write = fopen("template_time.dat", "wb");
        fwrite($file_write, $time_old);
        fclose($file_write);
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
    echo "url:$durl\nr:$r\n";
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
    echo "up_0:" . $data_file[1] . "\n";
    if (time() < $data_file[1]) {
        $access_token = $data_file[0];
        $time_expires_in = $data_file[1];
    } else {
        $appid = "wx691945ff03ba6040";
        $appsecret = "1e22eb6471847adef6c330719a739773";
        $data = curl_request("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$appsecret");
        echo "data:" . $data . "\n";
        $data_json = json_decode($data, true);
        $access_token = $data_json["access_token"];
        echo "acc:" . $data_json["access_token"] . "\n";
        $time_expires_in = time() + $data_json["expires_in"] - 200;
        $file_write = fopen($file_name, "wb");
        fwrite($file_write, $access_token);
        fwrite($file_write, "\t");
        fwrite($file_write, $time_expires_in);
        fclose($file_write);
    }
}

?>