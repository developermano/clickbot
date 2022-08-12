<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>deposit for ad</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- Font Awesome -->
<link
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
rel="stylesheet"
/>
<!-- Google Fonts -->
<link
href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
rel="stylesheet"
/>
<!-- MDB -->
<link
href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.10.2/mdb.min.css"
rel="stylesheet"
/>


</head>
<body>
<div class="container">
      
<h1 class="text text-center text-primary">ad deposit</h1>


<form action="https://faucetpay.io/merchant/webscr" method="post">
    <input type="hidden" name="merchant_username" value="manodev">
    <br>
    <input type="hidden" name="item_description" value="ad spend">
    <br>
    

<label class="form-label" for="customrange">amount in TRX( change using 👇 range selector) </label>
<div class="range">
  <input type="range" class="form-range" min="1" max="20" id="customrange" name="amount1" />
</div>


    <br>
    <input type="hidden" name="currency1" value="TRX">
    <br>
    <input type="hidden" name="currency2" value="">
    <br>
    <input type="hidden" name="custom" value="<?php echo $_GET['id']; ?>">
    <br>
    <input type="hidden" name="callback_url" value="https://faucetbank.xyz/confirm.php">
    <br>
    <input type="hidden" name="success_url" value="https://faucetbank.xyz/success.html">
    <br>
    <input type="hidden" name="cancel_url" value="https://faucetbank.xyz/failed.html">
    <br>
   <div class="text-center">
    <input id="makebtn" type="submit" class="btn btn-primary text-center" name="submit" value="Make Payment (10TRX)">
    </div>
</form>
</div>



<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<!-- MDB -->
<script
  type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.10.2/mdb.min.js"
></script>

<script>
setInterval(function() { 
    value1=$('#customrange').val(); 
    $("#makebtn").val("Make Payment ("+value1+"TRX)");
    }, 1000);
</script>



</body>
</html>