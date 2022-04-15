<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Search</title>
    </head>
    <body>
        <h1>Search</h1>
        <form action="search.php" method="post">
            <label for="search">Search</label>
            <input type="text" name="search" id="search">
            <input type="submit" value="Search">
        </form>
    </body>
</html>

<?php
if (isset($_POST['search'])) {
    $search = $_POST['search'];

    $sql = "SELECT * FROM listings WHERE title LIKE '%$search%'";
    $result = mysqli_query($link, $sql);
    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            echo $row['title'] . "<br>";
        }
    } else {
        echo "No results found";
    }
}
?>