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
                $data = $this->curl_get_contents($durl);
                $data_json = json_decode($data, true);
                $value = $data_json["value"];
                $contentStr = "传感器报警！当前数值为 : $value \n\n测试curl中:\n$data";
                if (time() > $this->time_expires_in) {
                    $this->update_access_token();
                }
                $contentStr .= " \n\naccess_token:$this->access_token";

                $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                echo $resultStr;
            } else {
                echo "Input something...";
            }

        } else {
            echo "lalala";
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

    private function curl_get_contents($durl)
    {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $durl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);//获取数据返回
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
            $data = $this->curl_get_contents("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$appsecret");
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


}

?>