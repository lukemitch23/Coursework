<!DOCTYPE html>
<html lang="en">
    <head>
         <meta charset="UTF-8">
         <title>Register</title>
    </head>
    <body>
        <h1>Register</h1>
        <form action="register.php" method="post">
            <label for="username">Username</label>
            <input type="text" name="uname" id="username">
            <label for="password">Password</label>
            <input type="password" name="psswd" id="password">
            <label for="email">Email</label>
            <input type="email" name="email" id="email">
            <input type="submit" value="Register">
        </form>
    </body>
</html>

<?php
// send form data to database
include 'db_connect.php';

// add the data to the database
if (isset($_POST['uname']) && isset($_POST['psswd']) && isset($_POST['email'])) {
    $uname = $_POST['uname'];
    $psswd = $_POST['psswd'];
    $email = $_POST['email'];
    $sql = "INSERT INTO users (username, password, email) VALUES ('$uname', '$psswd', '$email')";
    $result = mysqli_query($link, $sql);
    if ($result) {
        echo "Registration successful";
        // send user back to index.php
        header("Location: home.php");
    } else {
        echo "Registration failed";
    }
}
