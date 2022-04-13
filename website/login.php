<!DOCTYPE html>
<html lang="en">
    <head>
         <meta charset="UTF-8">
         <title>Login</title>
    </head>
    <body>
        <h1>Login</h1>
        <form action="login.php" method="post">
            <label for="username">Username</label>
            <input type="text" name="uname" id="username">
            <label for="password">Password</label>
            <input type="password" name="psswd" id="password">
            <input type="submit" value="Login">
        </form>
    </body>
</html>

<?php

include 'db_connect.php';

if (isset($_POST['uname']) && isset($_POST['psswd'])) {
    $uname = $_POST['uname'];
    $psswd = $_POST['psswd'];
    $sql = "SELECT * FROM users WHERE username = '$uname' AND password = '$psswd'";
    $result = mysqli_query($link, $sql);
    if (mysqli_num_rows($result) > 0) {
        echo "Login successful";
        // send user to home.php
        header("Location: home.php");
    } else {
        echo "Login failed";
    }
}
?>
