<?php
include "../../database/config.php";
$sql = "SELECT * from werknemer";
foreach ($pdo->query($sql) as $row) {
    ?>
    <a class="dropdown-item" href="../../pages/beer.php?userid=<?= $row['userid'];?>" ><?php echo $row['naam']?></a>
    <?php
} // end foreach
?>