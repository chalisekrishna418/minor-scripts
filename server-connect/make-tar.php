<?php 
	//$filename = $_GET['file'];
	echo "STARTING \n";
	$filename="mid";
	$command = "tar -zcvf " . $filename . ".tar.gz" . " ..\n";
	echo "$command";
	$cmd=shell_exec("$command");
	echo "Tar created \n";
	$command2="mv ../" . $filename . ".tar.gz" . " .";
	echo "$command2";
	$cmd2=shell_exec("$command2");
	echo "PROCESS COMPLETE \n";
	echo "YOU CAN NOW DOWNLOAD IT..."
?>
