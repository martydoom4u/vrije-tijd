<?php


include_once "../../database/config.php";

$query = "
SELECT * FROM beer 
";
$statement = $pdo->prepare($query);
$statement->execute();
$result = $statement->fetchAll();
$output = '';
foreach($result as $row)
{
    $rating = count_rating($row['beerid'], $pdo);
    $color = '';
    $output .= '
 <h3 class="text-primary">'.$row['naam'].'</h3>
 <ul class="list-inline" data-rating="'.$rating.'" title="Average Rating - '.$rating.'">
 ';

    for($count=1; $count<=5; $count++)
    {
        if($count <= $rating)
        {
            $color = 'color:#ffcc00;';
        }
        else
        {
            $color = 'color:#ccc;';
        }
        $output .= '<li title="'.$count.'" beerid="'.$row['beerid'].'-'.$count.'" data-index="'.$count.'"  data-beerid="'.$row['beerid'].'" data-rating="'.$rating.'" class="rating" style="cursor:pointer; '.$color.' font-size:16px;">&#9733;</li>';   }
    $output .= '
 </ul>
  <p>'.$row["tagline"].'</p>
  
 <p>'.$row["omschrijving"].'</p>
 <label style="text-danger">'.$row["alcohol"].'%</label>
 <hr />
 ';
}
echo $output;

function count_rating($beerid, $pdo)
{
    $output = 0;
    $query = "SELECT AVG(rating) as rating FROM rating WHERE beerid = '".$beerid."'";
    $statement = $pdo->prepare($query);
    $statement->execute();
    $result = $statement->fetchAll();
    $total_row = $statement->rowCount();
    if($total_row > 0)
    {
        foreach($result as $row)
        {
            $output = round($row["rating"]);
        }
    }
    return $output;
}


?>

