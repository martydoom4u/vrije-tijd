<?Php
require '../../database/config.php';
$url = file_get_contents("https://api.punkapi.com/v2/beers");
$client = curl_init($url);
curl_setopt($client,CURLOPT_RETURNTRANSFER,true);
$response = curl_exec($client);
$json = json_decode($url, true);



foreach ($json as $row) {
    $id = $row['id'];
    $name = $row['name'];
    $tagline = $row['tagline'];
    $omscrijving = $row['description'];
    $abv = $row['abv'];
    $image_url = $row['image_url'];

    // $alchol = $row['al'];
    // $beoordeling = $row['rv'];


    $query = "INSERT INTO beer (beerid, naam, tagline, omschrijving, alcohol, image_url) VALUES('$id', '$name', '$tagline', '$omscrijving', '$abv', '$image_url')";

    $dataatodb = mysqli_query($conn, $query);

    if (!$dataatodb) {
        //die("Error" . mysqli_error($conn));

    }


}
header("location: ../../pages/beer.php");

