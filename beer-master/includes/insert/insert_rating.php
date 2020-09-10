<?php

//fetch.php
include_once "../../database/config.php";

if(isset($_POST["index"], $_POST["beerid"], $_POST["userid"]))
{
    $query = "
 INSERT INTO rating(beerid, rating, userid) 
 VALUES (:beerid, :rating, :userid)
 ";
    $statement = $pdo->prepare($query);
    $statement->execute(
        array(
            ':beerid'   =>  $_POST["beerid"],
            ':rating'   => $_POST["index"],
            ':userid'   =>  $_POST["userid"],

        )
    );
    $result = $statement->fetchAll();
    if(isset($result))
    {
        echo 'done';
    }
}


?>
