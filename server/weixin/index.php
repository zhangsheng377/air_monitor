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
                $time = time();
                $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
                if (!empty($keyword)) {
                    $msgType = "text";

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

                    $dbhandle = sqlite_open('sqlitedb.db');
                    $query = sqlite_query($dbhandle, 'SELECT name FROM sensor_names');
                    sqlite_close($dbhandle);
                    $result = sqlite_fetch_all($query);
                    foreach ($result as $entry) {
                        $name = $entry['name'];
                        $contentStr .= "\n$name";
                    }
                    $dbhandle = sqlite_open('sqlitedb.db');
                    $query = sqlite_query($dbhandle, 'SELECT * FROM devices');
                    sqlite_close($dbhandle);
                    $result = sqlite_fetch_all($query);
                    foreach ($result as $entry) {
                        $contentStr = $contentStr . "\n" . $entry['device_id'] . "  " . $entry['location_x'] . "  " . $entry['location_y'] . "  " . $entry['sensor_PM2.5'] . "  " . $entry['sensor_CO'] . "  " . $entry['sensor_SO2'] . "  " . $entry['sensor_O3'];
                    }
                    $dbhandle = sqlite_open('sqlitedb.db');
                    $query = sqlite_query($dbhandle, 'SELECT COUNT(name) FROM sensor_names');
                    sqlite_close($dbhandle);
                    $result = sqlite_fetch_all($query);
                    $contentStr = $contentStr . "\n\n" . $result[0]["COUNT(name)"];


                    $dbhandle = sqlite_open('sqlitedb.db');
                    $query = sqlite_query($dbhandle, 'SELECT * FROM users');
                    sqlite_close($dbhandle);
                    $result = sqlite_fetch_all($query);
                    foreach ($result as $entry) {
                        $contentStr = $contentStr . "\n" . $entry['openid'] . "  " . $entry['device_id'] . "  " . $entry['PM2.5_limit'] . "  " . $entry['CO_limit'] . "  " . $entry['SO2_limit'] . "  " . $entry['O3_limit'];
                    }


                    $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                    echo $resultStr;


                } else {
                    echo "Input something...";
                }
            } elseif ($msgType == "event") {
                $event = $postObj->Event;
                if ($event == "LOCATION") {
                    $latitude = $postObj->Latitude;
                    $longitude = $postObj->Longitude;

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
                    $contentStr .= "\n\n$latitude";
                    $contentStr .= "\n\n$longitude";
                    $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                    //echo $resultStr;
                } elseif ($event == "CLICK") {
                    $eventkey = $postObj->EventKey;

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
                    $contentStr .= "\n\n$eventkey";
                    $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                    echo $resultStr;
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
                        //$contentStr .= "\n$id\n";
                        $dbhandle = sqlite_open('sqlitedb.db');
                        $query = sqlite_query($dbhandle, "SELECT COUNT(openid) FROM users WHERE openid=='$id'");
                        sqlite_close($dbhandle);
                        $result = sqlite_fetch_all($query);
                        if ($result[0]["COUNT(openid)"] == "0") {
                            $dbhandle = sqlite_open('sqlitedb.db');
                            $is_exec = sqlite_exec($dbhandle, "INSERT INTO users VALUES('$id','354298',70.0,120.0,40.0,99999.0)", $error);
                            sqlite_close($dbhandle);
                            if (!$is_exec) {
                                $contentStr .= "\nINSERT $id error : $error\n";
                            } else {
                                $contentStr .= "\nINSERT $id success\n";
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
                $contentStr .= "\n\n$location_x";
                $contentStr .= "\n\n$location_y";
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

    private
    function checkSignature()
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

    private
    function curl_request($durl, $data = null)
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

    private
    function update_access_token()
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

    private
    function get_openids()
    {
        $this->update_access_token();
        $data_return = $this->curl_request("https://api.weixin.qq.com/cgi-bin/user/get?access_token=$this->access_token&next_openid=");
        $ids_json = json_decode($data_return, true);
        return $ids_json["data"]["openid"];
    }


}

?>