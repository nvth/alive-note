```php
query : select id from prob_troll where id=''
<?php  
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  if(preg_match("/admin/", $_GET[id])) exit("HeHe");
  $query = "select id from prob_troll where id='{$_GET[id]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id'] == 'admin') solve("troll");
  highlight_file(__FILE__);
?>
```

Explain:

Filter `admin` but not case sensitive, 
```php
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~"); //ignore under/upper case 
  if(preg_match("/admin/", $_GET[id])) exit("HeHe"); // filter admin only
```

Payload: `Admin`

