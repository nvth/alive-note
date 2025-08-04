```php
query : select id from prob_vampire where id=''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  $_GET[id] = strtolower($_GET[id]);
  $_GET[id] = str_replace("admin","",$_GET[id]); 
  $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("vampire"); 
  highlight_file(__FILE__); 
?>
```

Explain:

```php
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~"); // filter single quotes
  $_GET[id] = strtolower($_GET[id]); // convert input character to lower case
  $_GET[id] = str_replace("admin","",$_GET[id]); // replace admin to whitespace
```

Solve:

Let's using `adAdminmin`, this strtolower() and str_replace() will convert to lower and remove `Admin` and i got `admin`

