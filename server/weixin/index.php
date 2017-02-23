<?php
/**
 * wechat php test
 */

//define your token
define("TOKEN", "weixin");
$wechatObj = new wechatCallbackapiTest();
if (!isset($_GET['echostr'])) {
    $wechatObj->responseMsg();
} else {
    $wechatObj->valid();
}

class wechatCallbackapiTest
{
    private $access_token = "";
    private $time_expires_in = -1;

    public function valid()
    {
        $echoStr = $_GET["echostr"];

        //valid signature , option
        if ($this->checkSignature()) {
            echo $echoStr;
            exit;
        }
    }

    /**
     *
     */
    public function responseMsg()
    {
        //get post data, May be due to the different environments
        $postStr = $GLOBALS["HTTP_RAW_POST_DATA"];

        //extract post data
        if (!empty($postStr)) {
            /* libxml_disable_entity_loader is to prevent XML eXternal Entity Injection,
               the best way is to check the validity of xml by yourself */
            libxml_disable_entity_loader(true);
            $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
            $fromUsername = $postObj->FromUserName;
            $toUsername = $postObj->ToUserName;
            $msgType = $postObj->MsgType;
            if ($msgType == "text") {
                $keyword = trim($postObj->Content);
                if ($keyword == "debug") {
                    $time = time();
                    $msgType = "text";
                    $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";

                    $device_id = 353097;
                    $sensor_id = 397985;
                    $durl = "http://api.yeelink.net/v1.0/device/$device_id/sensor/$sensor_id/datapoints";
                    //$data = file_get_contents($durl);
                    //$data_json=json_decode($data,true);
                    //$contentStr='传感器报警！当前数值为 : '.$data_json["value"];
                    //$data_json = json_decode($data);
                    //$r = $this->curl_file_get_contents($durl);
                    //$contentStr = "传感器报警！当前数值为 : $data_json->value \n\n测试curl中:\n$r";
                    $data = $this->curl_request($durl);
                    $data_json = json_decode($data, true);
                    $value = $data_json["value"];
                    $contentStr = "传感器报警！当前数值为 : $value";
                    if (time() > $this->time_expires_in) {
                        $this->update_access_token();
                    }
                    //$contentStr .= "\n\naccess_token:$this->access_token";
                    $template = array('touser' => "$fromUsername", 'template_id' => "Oh5bDFWIIdg8acICj639FGPeLNMNxP0X68uWykjZLuM", 'url' => "http://github.com/zhangsheng377", 'data' => array('first' => array('value' => urlencode("传感器报警！"), 'color' => "#743A3A"), 'second' => array('value' => urlencode("$value"), 'color' => "#FF0000")));
                    $data_template = $this->curl_request("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=$this->access_token", urldecode(json_encode($template)));
                    $contentStr .= "\n\ntemplate:$data_template";
                    //$contentStr .= "\n\nfromUsername:$fromUsername\ntoUsername:$toUsername";
                    $ids = $this->get_openids();
                    $count_ids = count($ids);
                    $contentStr .= "\n\n$count_ids  $ids[0]";

                    $sql_command = "SELECT name FROM sensor_names";
                    $query = $this->mysqlite_do($sql_command);
                    $result = sqlite_fetch_all($query);
                    foreach ($result as $entry) {
                        $name = $entry['name'];
                        $contentStr .= "\n$name";
                    }
                    $sql_command = "SELECT * FROM devices";
                    $query = $this->mysqlite_do($sql_command);
                    $result = sqlite_fetch_all($query);
                    foreach ($result as $entry) {
                        $contentStr = $contentStr . "\n" . $entry['device_id'] . "  " . $entry['location_x'] . "  " . $entry['location_y'] . "  " . $entry['sensor_PM2.5'] . "  " . $entry['sensor_CO'] . "  " . $entry['sensor_SO2'] . "  " . $entry['sensor_O3'];
                    }
                    $sql_command = "SELECT COUNT(name) FROM sensor_names";
                    $query = $this->mysqlite_do($sql_command);
                    $result = sqlite_fetch_all($query);
                    $contentStr = $contentStr . "\n\n" . $result[0]["COUNT(name)"];

                    $sql_command = "SELECT * FROM users";
                    $query = $this->mysqlite_do($sql_command);
                    $result = sqlite_fetch_all($query);
                    foreach ($result as $entry) {
                        $contentStr = $contentStr . "\n" . $entry['openid'] . "  " . $entry['device_id'] . "  " . $entry['PM2.5_limit'] . "  " . $entry['CO_limit'] . "  " . $entry['SO2_limit'] . "  " . $entry['O3_limit'];
                    }

                    $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                    echo $resultStr;

                } else {
                    $this->update_access_token();
                    $str = explode(' ', $keyword);
                    if ($str[0] == "debug广播") {
                        $ids = $this->get_openids();
                        foreach ($ids as $id) {
                            $template = array(
                                'touser' => "$id",
                                'template_id' => "hhfH9JOdwlcRhPhsjcixtd9EvSFOADgw-BFCUUD01v4",
                                'data' => array(
                                    'first' => array('value' => urlencode("$str[1]"), 'color' => "#743A3A")
                                )
                            );
                            $this->curl_request("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=$this->access_token", urldecode(json_encode($template)));
                        }
                    } else {
                        $sensor_name = $str[0];
                        if ($sensor_name == "PM2.5") {
                            $sensor_name = "PM2_5";
                        }
                        $limit_sensor = $sensor_name . "_limit";
                        $value = (double)$str[1];
                        $sql_command = "UPDATE users SET $limit_sensor = $value WHERE openid=='$fromUsername'";
                        $is_exec = $this->mysqlite_do($sql_command, $error);
                        if ($is_exec) {
                            $contentStr = "您的$str[0]报警阈值已设置成功";
                        } else {
                            $contentStr = "对不起，您的$str[0]报警阈值修改失败...\n\n请向客服QQ:435878393反馈此错误代码~谢谢~~\n\n$sql_command\n\n$error";
                        }

                        $time = time();
                        $msgType = "text";
                        $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                        $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                        echo $resultStr;
                    }
                }
            } elseif ($msgType == "event") {
                $event = $postObj->Event;
                if ($event == "LOCATION") {
                    $latitude = $postObj->Latitude;
                    $longitude = $postObj->Longitude;
                    $this->mysqlite_device_id_closest($latitude, $longitude, $fromUsername, true);
                } elseif ($event == "CLICK") {
                    $eventkey = $postObj->EventKey;
                    if ($eventkey == "showlimit") {
                        $contentStr = "您所设置的空气质量报警阈值为 : ";
                        $sql_command = "SELECT name FROM sensor_names";
                        $query = $this->mysqlite_do($sql_command);
                        $sensor_names = sqlite_fetch_all($query);
                        foreach ($sensor_names as $sensor_name) {
                            $sql_command = "SELECT $sensor_name[0]_limit FROM users WHERE openid=='$fromUsername'";
                            $query = $this->mysqlite_do($sql_command);
                            $result = sqlite_fetch_all($query);
                            $limit_value = $result[0]["$sensor_name[0]_limit"];
                            if ($sensor_name[0] == "PM2_5") {
                                $contentStr .= "\nPM2.5 : $limit_value";
                            } else {
                                $contentStr .= "\n$sensor_name[0] : $limit_value";
                            }
                        }
                        $time = time();
                        $msgType = "text";
                        $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                        $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                        echo $resultStr;
                    } elseif ($eventkey == "setlimit") {
                        $template = array(
                            'touser' => "$fromUsername",
                            'template_id' => "T10MoD6iWTsqf9h-q9bjEAcEBIytb5traQrNNZZKjDs",
                            'data' => array(
                                'first' => array(
                                    'value' => urlencode("由于微信的限制，目前我们只能请您采取发送命令的方式进行设置阈值。对给您造成的不便，我们感到万分抱歉。"),
                                    'color' => "#000000"),
                                'second' => array(
                                    'value' => urlencode("监测类型 报警阈值"),
                                    'color' => "#00FF00"),
                                'third' => array(
                                    'value' => urlencode("PM2.5 56.7"),
                                    'color' => "#0000FF"),
                                'fourth' => array(
                                    'value' => urlencode("目前所支持的监测类型有：PM2.5、CO、SO2、O3"),
                                    'color' => "#000000")
                            )
                        );
                        $this->update_access_token();
                        $data_template = $this->curl_request("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=$this->access_token", urldecode(json_encode($template)));
                    } else {
                        $contentStr = "点击事件 $eventkey 暂时未被收录\n\n请联系系统管理员：435878393";
                        $time = time();
                        $msgType = "text";
                        $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                        $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                        echo $resultStr;
                    }


                } elseif ($event == "subscribe") {
                    $time = time();
                    $msgType = "text";
                    $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";

                    $ids = $this->get_openids();
                    $count_ids = count($ids);
                    $contentStr = "现在一共有 $count_ids 位朋友关注了本公众号~";
                    foreach ($ids as $id) {
                        $sql_command = "SELECT COUNT(openid) FROM users WHERE openid=='$id'";
                        $query = $this->mysqlite_do($sql_command);
                        $result = sqlite_fetch_all($query);
                        if ($result[0]["COUNT(openid)"] == "0") {
                            $sql_command = "INSERT INTO users VALUES('$id','354298',70.0,120.0,40.0,99999.0)";
                            $is_exec = $this->mysqlite_do($sql_command, $error);
                            if ($is_exec) {
                                //$contentStr .= "\nINSERT $id success\n";
                            } else {
                                $contentStr .= "请向客服反馈此错误代码~谢谢~~\n\nINSERT $id error :\n$error";
                            }
                        }
                    }

                    $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                    echo $resultStr;
                } else {
                    $time = time();
                    $msgType = "text";
                    $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                    $contentStr = "$event";
                    $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                    echo $resultStr;
                }
            } elseif ($msgType == "location") {
                $msgType_old = $msgType;
                $location_x = $postObj->Location_X;
                $location_y = $postObj->Location_Y;
                $label = $postObj->Label;

                $device_id = $this->mysqlite_device_id_closest($location_x, $location_y, $fromUsername);

                $time = time();
                $msgType = "text";
                $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                $contentStr = "$label" . "的空气质量为 : ";

                $sql_command = "SELECT name FROM sensor_names";
                $query = $this->mysqlite_do($sql_command);
                $sensor_names = sqlite_fetch_all($query);
                //$value=array();
                foreach ($sensor_names as $sensor_name) {
                    $sql_command = "SELECT sensor_$sensor_name[0] FROM devices WHERE device_id=='$device_id'";
                    $query = $this->mysqlite_do($sql_command);
                    $result = sqlite_fetch_all($query);
                    $sensor_id = $result[0]["sensor_$sensor_name[0]"];
                    $value = $this->yeelinkapi_read_lastvalue($device_id, $sensor_id);
                    if ($sensor_name[0] == "PM2_5") {
                        $contentStr .= "\nPM2.5的数值为 : $value";
                    } else {
                        $contentStr .= "\n$sensor_name[0]的数值为 : $value";
                    }
                }

                $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                echo $resultStr;
            } else {
                $msgType_old = $msgType;

                $time = time();
                $msgType = "text";
                $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                $contentStr = "$msgType_old";
                $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                echo $resultStr;
            }
        } else {
            echo "postStr is empty";
            exit;
        }
    }

    private function checkSignature()
    {
        // you must define TOKEN by yourself
        if (!defined("TOKEN")) {
            throw new Exception('TOKEN is not defined!');
        }

        $signature = $_GET["signature"];
        $timestamp = $_GET["timestamp"];
        $nonce = $_GET["nonce"];

        $token = TOKEN;
        $tmpArr = array($token, $timestamp, $nonce);
        // use SORT_STRING rule
        sort($tmpArr, SORT_STRING);
        $tmpStr = implode($tmpArr);
        $tmpStr = sha1($tmpStr);

        if ($tmpStr == $signature) {
            return true;
        } else {
            return false;
        }
    }

    private function curl_request($durl, $data = null)
    {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $durl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);//获取数据返回
        if (!empty($data)) {
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        }
        $r = curl_exec($ch);
        curl_close($ch);
        return $r;
    }

    private function update_access_token()
    {
        $file_name = "access_token.dat";
        $file_read = fopen($file_name, "rb");
        $data_file = fscanf($file_read, "%s\t%d");
        fclose($file_read);
        if (time() < $data_file[1]) {
            $this->access_token = $data_file[0];
            $this->time_expires_in = $data_file[1];
        } else {
            $appid = "wx691945ff03ba6040";
            $appsecret = "1e22eb6471847adef6c330719a739773";
            $data = $this->curl_request("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$appsecret");
            $data_json = json_decode($data, true);
            $this->access_token = $data_json["access_token"];
            $this->time_expires_in = time() + $data_json["expires_in"] - 200;
            $file_write = fopen($file_name, "wb");
            fwrite($file_write, $this->access_token);
            fwrite($file_write, "\t");
            fwrite($file_write, $this->time_expires_in);
            fclose($file_write);
        }
    }

    private function get_openids()
    {
        $this->update_access_token();
        $data_return = $this->curl_request("https://api.weixin.qq.com/cgi-bin/user/get?access_token=$this->access_token&next_openid=");
        $ids_json = json_decode($data_return, true);
        return $ids_json["data"]["openid"];
    }

    private function mysqlite_do($sql_command, &$error = null)
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

    private function mysqlite_device_id_closest($location_x, $location_y, $openid = null, $is_update = false)
    {
        if (empty($openid)) {
            $device_id = "354298";
        } else {
            $sql_command = "SELECT device_id FROM users WHERE openid=='$openid'";
            $query = $this->mysqlite_do($sql_command);
            $result = sqlite_fetch_all($query);
            $device_id = $result[0]["device_id"];
        }
        $distance = 9999999;
        $sql_command = "SELECT device_id,location_x,location_y FROM devices";
        $query = $this->mysqlite_do($sql_command);
        $result = sqlite_fetch_all($query);
        foreach ($result as $entry) {
            $gap_x = (double)$location_x - $entry['location_x'];
            $gap_y = (double)$location_y - $entry['location_y'];
            $distance_new = pow($gap_x, 2) + pow($gap_y, 2);
            if ($distance_new < $distance) {
                $distance = $distance_new;
                $device_id = $entry['device_id'];
            }
        }
        if ($is_update) {
            $sql_command = "UPDATE users SET device_id='$device_id' WHERE openid=='$openid'";
            $this->mysqlite_do($sql_command);
        }
        return $device_id;
    }

    private function yeelinkapi_read_lastvalue($device_id, $sensor_id)
    {
        $durl = "http://api.yeelink.net/v1.0/device/$device_id/sensor/$sensor_id/datapoints";
        $data = $this->curl_request($durl);
        $data_json = json_decode($data, true);
        return $data_json["value"];
    }

}

?>