<?php
if (date('H') > 17){
    ?>
    <!DOCTYPE html>
    <h1 style="color: green"; align="center"><?php echo 'er mag gedronken worden'?><i class="fas fa-beer"></i><i class="fas fa-beer"></i><i class="fas fa-beer"></i></h1>
    <?php
}else{
    ?>
    <!DOCTYPE html>
    <h1 style="color: red"; align="center"><?php echo 'het is nog geen tijd voor bier'?></h1>
    <?php
}
?>