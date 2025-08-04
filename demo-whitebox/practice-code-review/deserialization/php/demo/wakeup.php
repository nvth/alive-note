<?php
class User{
  public $username;
  public $status;
  public function __wakeup()
  {
      echo "__wakeup() method calling";
  }
}
$user = new User;
$user->username = 'vickie';
$user->status = 'not admin';
$serialized_string = serialize($user);
unserialize($serialized_string);
?>