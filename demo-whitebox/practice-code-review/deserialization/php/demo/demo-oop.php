<?php
class User{
  public $id;
  public $username;
  public $role;
  public $verify;
   
}
$user = new User;
$user->id = 1;
$user->username = 'kevin24';
$user->role = 'admin';
$user->verify = true;
$serializedUser = serialize($user);
echo "String early: \n";
echo $serializedUser;
echo "\n";
echo "String after that\n";
var_dump(unserialize($serializedUser));
?>