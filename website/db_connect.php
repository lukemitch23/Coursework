<?php
define('DB_SERVER', '192.168.0.45');
define('DB_USERNAME', 'server');
define('DB_PASSWORD', 'server123');
define('DB_NAME', 'site');

$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>
