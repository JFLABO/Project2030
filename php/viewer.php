<?php
//JSONオブジェクトをバインドして表示するロジック　基本設計
//JSONファイルをバインド　それを読み込み表示する　サイトマップ自動生成
//$bind="../data/filenme.json";
$bind="./data/136-0071_2-13-12_2022121209:28:38.json";
//JSONをパース
$json = file_get_contents($bind);
//$json = mb_convert_encoding($json, 'UTF8', 'ASCII,JIS,UTF-8,EUC-JP,SJIS-WIN');
$arr = json_decode($json,true);
?>
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
<div data-role="page" data-title="たびれぽ福分け取材班 TIPS">

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
  <?php //JSONを表示
  //echo $arr['res']['blogData']['id'];
  //echo $arr->res->blogData->id;

  ?>
  <span id="title"><?php //JSONを表示
  echo $arr['title'];?></span>
  <HR>
  <span id="contents"><?php //JSONを表示
  echo $arr['content'];?></span>
  <HR>
  <span id="project"><?php //JSONを表示
  echo $arr['project'];?></span>
  <HR>
  <span id="kanri">経営管理コード</span>
  <HR>
  <span id="date"><?php //JSONを表示
  echo $arr['date'];?></span>
</div><BR>
<a href="list.php" class="ui-btn" data-ajax="false">一覧</a>
  </div>

  <div data-role="footer">
    <h3>Copyright1981-2022</h3>
  </div>

</div>
</CENTER>

</body>
