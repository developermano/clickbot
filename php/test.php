<?php

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

echo $newamount;


?>