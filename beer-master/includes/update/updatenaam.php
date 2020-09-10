<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script src="https://kit.fontawesome.com/77d30a9fc9.js" crossorigin="anonymous"></script>

</head>
<body>
<div class="jumbotron text-center">
    <h1><i class="fas fa-beer"></i> welkom bij  Bier beoordeling <i class="fas fa-beer"></i></h1>
</div>
<div class="container text-center">
    <div class="row">
        <div class="col-md-12">
            <form action="beoordeling.php" method="post">
                <input type="text"  class="form-control" placeholder="uw naam"   name="name" id="name" style="border-color:black;" required>
                <button type="submit" class="btn btn-primary">verzenden</button>
            </form>
         </div>
    </div>
</div>