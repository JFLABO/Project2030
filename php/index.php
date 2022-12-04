<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<?php require('actmoni.php') ?>
<link rel="stylesheet" href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" />
<script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
<script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
<meta charset="utf-8">
<body>

<!--ページ領域-->
<div data-role="page" data-title="jQuery Mobile TIPS">

  <!--ヘッダー領域-->
  <div data-role="header">
    <h1>JFLABO:たびれぽ</h1>
  </div>

  <div role="main" class="ui-content">
  ようこそいらっしゃいました。

<CENTER>
<a href="http://rb.toki.fun/fx.htm" class="ui-btn" data-ajax="false">戻る</a>

<div class="box10">
  <style>
.box10 {
    padding: 0.5em 1em;
    margin: 2em 0;
    color: #00BCD4;
    background: #e4fcff;/*背景色*/
    border-top: solid 6px #1dc1d6;
    box-shadow: 0 3px 4px rgba(0, 0, 0, 0.32);/*影*/
}
.box10 p {
    margin: 0;
    padding: 0;
}
</style>
  <span id="title">ここに文章</span>
  <HR>
  <span id="contents">ここに文章</span>
  <HR>
  <span id="project">ここに文章</span>
  <HR>
  <span id="kanri">経営管理コード</span>
  <HR>
  <span id="date">経営管理コード</span>
</div><BR>
<a href="list.php" class="ui-btn" data-ajax="false">一覧</a>

<!--
<input type="text"><BR>
<button id="send">たーのしー！</button>
-->
<?php
/*
foreach (glob("/var/www/html/jlog/data/*.json") as $filename) {
echo "<a href='index.php?u=";
echo $filename;
echo "' data-ajax='false'>";
         echo $filename;
         echo "</a><br/><br/>";
}
*/
?>
  </div>

  <div data-role="footer">
    <h3>Copyright1981-2022</h3>
  </div>

</div>
<script>
  //ファイル名を受け取る
    <?php
  if($_GET['u']){
      $str=str_replace("/var/www/html/jlog/data/", '',$_GET['u']);
                       echo 'fn="'.$str.'";';

  }else{
      echo 'fn="136-0071_2-13-12_2022120414:32:29.json";';

  }
    ?>
//fnがあれば代入する fnが無ければいれる
  //fn="136-0071_2-13-12_2022120414:32:29.json";

//POSTで値を渡す　読み取り　送信　ページ遷移
$("#title").text("変更後の文章");
$("#contents").text("変更後の文章");
  $(function () {

  var data = []; // data配列を定義
  $.ajax({
    // ajax読み込みの設定
    type: "GET",
    url: "http://unit213.tabirepo.online/jlog/data/"+fn, // jsonまでのファイルパス
    dataType: "json", // ファイル形式
    async: false, // 非同期通信フラグ
  }).then(
    function (json) {
        var data3 = JSON.stringify(json);
        $("#title").text(json["title"]);
        $("#contents").text(json["content"]);
        $("#project").text(json["project"]);
        $("#date").text(json["date"]);
        $("#kanri").text(json["KANRICODE"]);

        // jsonの読み込みに成功
      console.log("読み込みに成功しました");
    },
    function () {
      // jsonの読み込みに失敗
      console.log("読み込みに失敗しました");
    }
  );
});
</script>

</body>
</CENTER>
