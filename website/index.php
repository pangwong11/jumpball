<?php
  $location = "http://" . $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']."t/?pg=home";
  header("Location: $location");
  die;
?>
