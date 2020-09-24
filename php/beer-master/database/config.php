<?php

$pdo = new PDO('mysql:host=localhost;dbname=bier', 'root', 'root');

$servername = "localhost";
$username = "root";
$password = "root";
$database = "bier";

// Create connection
$conn = mysqli_connect($servername, $username, $password,$database);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}