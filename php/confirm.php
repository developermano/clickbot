<?php

include_once'db.php';

$token = $_POST['token'];

$payment_info = file_get_contents("https://faucetpay.io/merchant/get-payment/" . $token);
$payment_info = json_decode($payment_info, true);
$token_status = $payment_info['valid'];

$merchant_username = $payment_info['merchant_username'];
$amount1 = $payment_info['amount1'];
$currency1 = $payment_info['currency1'];
$amount2 = $payment_info['amount2'];
$currency2 = $payment_info['currency2'];
$custom = $payment_info['custom'];

$my_username = "manodev";

if ($my_username == $merchant_username && $token_status == true) {



    include_once'db.php';

    $stmt1 = $conn->prepare(" SELECT * FROM `ad` WHERE campaignid=?");
    $stmt1->bind_param("s", $custom);
    $stmt1->execute();
    $result = $stmt1->get_result();

    $examount=mysqli_fetch_row($result)[6];

    $newamount=$examount+$amount;
   

$stmt1 = $conn->prepare("UPDATE `ad` SET `totalbudget` = ? WHERE campaignid = ?;");
$stmt1->bind_param("ss",$newamount,$custom);
$stmt1->execute();


} else {

    echo 'thank you hacker , try other sites';

}