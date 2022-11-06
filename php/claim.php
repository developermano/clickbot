<?php

include_once'db.php';


function sendreward($userid){
    

$data = array(
    'api_key' => "d4bbecbaceaec2a435165349e3404b84a89e8ba0",
    'to' => $userid,
    'amount'=> 1000000
);


$cURLConnection = curl_init('https://faucetpay.io/api/v1/send');
curl_setopt($cURLConnection, CURLOPT_POSTFIELDS, $data);
curl_setopt($cURLConnection, CURLOPT_RETURNTRANSFER, true);

$apiResponse = curl_exec($cURLConnection);
curl_close($cURLConnection);

return $apiResponse;
}


$id=$_GET['id'];
$stmt = $conn->prepare("SELECT * FROM `shortenlink` WHERE k=?");
$stmt->bind_param("s", $id);
$stmt->execute();
$result = $stmt->get_result();


if ($result->num_rows > 0) {
  //give reward
  while($row = $result->fetch_assoc()) {
    

$userwallet="0";
$stmt1 = $conn->prepare("SELECT * FROM `user` WHERE userid=?");
$stmt1->bind_param("s", $row['v']);
$stmt1->execute();
$result = $stmt1->get_result();



  while($row = $result->fetch_assoc()) {
$userwallet=$row['walletaddress'];
  }
    





  }
  sendreward($userwallet);
  echo "REWARD IS SENT TO YOUR WALLET";
  $sql = "DELETE FROM url WHERE urlid='{$id}'";
  $result = $conn->query($sql);
} else {
  echo "THE REWARD IS CLAIMED ALREADY";
}
$conn->close();



?>