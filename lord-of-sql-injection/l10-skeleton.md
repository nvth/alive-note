```php
query : select id from prob_skeleton where id='guest' and pw='' and 1=0
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("skeleton"); 
  highlight_file(__FILE__); 
?>
```

Explain:

```php 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0";  // and make condition this query return false, not solv this lab
```
this $query above meaning: select id from prob_skeleton table with id is guest and pw is my input and 1=0,

`and` make query always return `false` because `and` make satisfy all conditions, `1=0 `ís false condition 

bypass this using `or` operator, `or` operator just get data when query satisfy only one condition not all conditions like `and` operator

Payload: `' or id = 'admin' or ''='`

Explain payload: 

this payload will select id is admin regardless of other conditions. That is the difference between `or` and `and`.

`or ''='` because this payload was put between single quotes so let bypass single quotes using payload. meaning `null string` compare `null string`

