<html>
<body>
<h3>summary结果如下：</h3>


<div id="bodyframe" >  
 <iframe src="
 <?php
  $vcompile=  $_GET["summary"];
  $vcompile=str_replace("%","%25",$vcompile);
  $vcompile="summary/".$vcompile;
  echo $vcompile
?>

"
 marginheight="0" marginwidth="0" frameborder="0" scrolling="no" width=100% height=100% id="iframepage" name="iframepage" onLoad="iFrameHeight()" ></iframe>

</div>

</body>
</div>
</html>
