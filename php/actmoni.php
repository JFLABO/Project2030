<?php
//アクションモニター仕様　JSONを生成する
//経営管理コード
//日時　ランダム .json
$s="136-0071_2-13-12_";
$dt=date("YmdH:i:s") ;
$dt2=date("Y/m/d H:i:s") ;
$str = 'abcdefghijklmnopqrstuvwxyz';
$rand_str = substr(str_shuffle($str), 0, 8);
//ファイル名
//最初書き込みできない　権限設定　書き込めるようにする

$fn="/var/www/html/jlog/actlog/".$s.$dt.$rand_str.".json";
$MCobj = [
       'type' => 'actlog',
       'referer'        =>       $_SERVER['HTTP_REFERER'],
       'remoteIP'         =>     $_SERVER["REMOTE_ADDR"],
       'time'             =>     $dt2
                                                  ];
$MCobj=json_encode($MCobj);
function write_obj(){
         file_put_contents($fn, $MCobj);
         }
try {
         file_put_contents($fn, $MCobj);
} catch (Exception $e) {
         file_put_contents($fn, $MCobj);
}
?>
