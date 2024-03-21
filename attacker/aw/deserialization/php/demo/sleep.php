<?php
class User{
  public $id;
  public $username;
  public $role;
  public $verify;
  public function __sleep() // chương trình chỉ trả về những thứ mà return ở sleep() dạng ["propertype","propertype"] khi serialize obj
  {
     return ["id", "username","role"];
  }
}

//get data 
$user = new User;
$user->id = 1;
$user->username = 'kevin24';
$user->role = 'admin';
$user->verify = true;
echo serialize($user);
?>