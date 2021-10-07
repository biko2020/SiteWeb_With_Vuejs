<?php

$email= $_POST['email'];
$subject = $_POST['subject'];
$message= $_POST['message'];
$to = "brahimlion38@mail.com";
$txt ="Email = ". $email . "\r\n  Sujet = " . $subject . "\r\n Message =" . $message;
$headers = "From: noreply@yoursite.com" . "\r\n" .
"CC: somebodyelse@example.com";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("Location:thanks.html");
?>