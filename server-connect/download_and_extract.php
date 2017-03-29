<?php 
	$url = $_GET['file'];
	//$filename="motherland";
	$getcmd = "wget " . $url;
	$cmd=shell_exec("$getcmd");
	$extractcmd = "tar -xvf " . filename;
	$cmd=shell_exec("$extractcmd");
	echo "PROCESS COMPLETE \n";
	echo "YOU CAN NOW CONFIGURE THE DATABASE"
?>
