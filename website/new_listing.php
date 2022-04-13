html page with a table that allows the user to enter the item name price start and end date along with description and minimum price
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Camera auction site</title>
    </head>
    <body>
        <h1>Camera auction site</h1>
        <h2>Please enter the item name, price, start and end date along with a description and minimum price</h2>
        <form action="new_listing.php" method="post">
            <label for="item_name">Item name</label>
            <input type="text" name="item_name" id="item_name">
            <label for="price">Price</label>
            <input type="text" name="price" id="price">
            <label for="start_date">Start date</label>
            <input type="text" name="start_date" id="start_date">
            <label for="end_date">End date</label>
            <input type="text" name="end_date" id="end_date">
            <label for="description">Description</label>
            <input type="text" name="description" id="description">
            <label for="min_price">Minimum price</label>
            <input type="text" name="min_price" id="min_price">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>

<?php

include 'db_connect.php';

if (isset($_POST['item_name']) && isset($_POST['price']) && isset($_POST['start_date']) && isset($_POST['end_date']) && isset($_POST['description']) && isset($_POST['min_price'])) {
    $item_name = $_POST['item_name'];
    $price = $_POST['price'];
    $start_date = $_POST['start_date'];
    $end_date = $_POST['end_date'];
    $description = $_POST['description'];
    $min_price = $_POST['min_price'];
    $sql = "INSERT INTO listings (item_name, price, start_date, end_date, description, min_price) VALUES ('$item_name', '$price', '$start_date', '$end_date', '$description', '$min_price')";
    $result = mysqli_query($link, $sql);
    if ($result) {
        echo "Listing added";

        header("Location: home.php");
    } else {
        echo "Listing failed";
    }
}
?>
