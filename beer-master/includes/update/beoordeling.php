<?php

$naam = $_POST['name'];
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "bier";
$rid = $_GET['rid'];


try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "INSERT INTO `werknemer` (naam) VALUES (:naam)";
    // Prepare statement
    $stmt = $conn->prepare($sql);
    // execute the query
    $stmt->execute([
        ':naam'=>$naam,

    ]);

    echo $stmt->rowCount() .   header("location: ../../index.php");
}
catch(PDOException $e)
{
}
$conn = null;