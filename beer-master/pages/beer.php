<?php

$id = $_GET['userid'];
echo $id;

include_once 'bierif.php';
?>
<head>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"/>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://kit.fontawesome.com/77d30a9fc9.js" crossorigin="anonymous"></script>
</head>
<body>
<div class="container " data-userid="<?php echo $id?>" style="width:800px;">
    <h2 align="center">Bier beoordeling</h2>


    <br />
    <span id="beer_list"></span>
    <a class="btn btn-danger text-center" href="../includes/data/data.php">update hier de biertjes </a>
    <br />

    <br />

</div>

</body>
</html>

<script>
    $(document).ready(function(){

        load_beer_data();

        function load_beer_data()
        {
            $.ajax({
                url:"../includes/data/fetch.php",
                method:"POST",
                success:function(data)
                {
                    $('#beer_list').html(data);
                }
            });
        }

        $(document).on('mouseenter', '.rating', function(){
            var index = $(this).data("index");
            var beerid = $(this).data('beerid');
            remove_background(beerid);
            for(var count = 1; count<=index; count++)
            {
                $('#'+beerid+'-'+count).css('color', '#ffcc00');
            }
        });

        function remove_background(beerid)
        {
            for(var count = 1; count <= 5; count++)
            {
                $('#'+beerid+'-'+count).css('color', '#ccc');
            }
        }

        $(document).on('mouseleave', '.rating', function(){
            var index = $(this).data("index");
            var beerid = $(this).data('beerid');
            var rating = $(this).data("rating");
            remove_background(beerid);

            for(var count = 1; count<=rating; count++)
            {
                $('#'+beerid+'-'+count).css('color', '#ffcc00');
            }
        });

        $(document).on('click', '.rating', function(){
            var index = $(this).data("index");
            var beerid = $(this).data('beerid');
            var userid = $('[data-userid]').data('userid');
            $.ajax({
                url:"../includes/insert/insert_rating.php",
                method:"POST",
                data:{index:index, beerid:beerid, userid:userid},
                success:function(data)
                {
                    if (data == 'done')
                    {
                        load_beer_data();
                        alert("uw heeft "+index +" van de 5 sterren gekozen");
                    }
                    else
                    {
                        alert("oppppps");

                    }
                }
            });

        });

    });






</script>