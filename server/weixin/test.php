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

$menu_json = '{
    "button":[
        {
            "name":"查询",
            "type":"location_select",
            "key":"lookfor"
        },
        {
            "name":"设置阈值",
            "type":"click",
            "key":"setlimit"
        }
    ]
    }';
$url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=$access_token";
$result = curl_request($url, $menu_json);
echo $result;

function curl_request($durl, $data = null)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $durl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);//获取数据返回
    if (!empty($data)) {
        //echo "curl_data:$data";
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

function get_openids()
{
    global $access_token;
    update_access_token();
    $data_return = curl_request("https://api.weixin.qq.com/cgi-bin/user/get?access_token=$access_token&next_openid=");
    $ids_json = json_decode($data_return, true);
    return $ids_json["data"]["openid"];
}

?>