```php
query : select id from prob_orc where id='admin' and pw=''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

Explain:

So, i just handle only `pw` parameter.

- check prob, ., _, () 
- /..../i : ignore lower and upper case

`pw` was put in on single quotes so, preg_match do not filter single quotes

$_GET[pw] = addslashes($_GET[pw])

https://www.php.net/manual/en/function.addslashes.php

```docs
 Returns a string with backslashes added before characters that need to be escaped. These characters are:

    single quote (')
    double quote (")
    backslash (\)
    NUL (the NUL byte)

```

`pw` params after got addslashes() like: `1 \' or 1=1#` so `pw` and `_GET[pw]` is not the same value, can not trigger ```solv("orc")```

so, i know, if true query it's. throw `admin`

```php
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
```

I already have true query LIKE: ``select id from prob_orc where id='admin' and pw='1' or 1=1#'``

let substr() to find password of admin.

So, if i want to using substr() I need guess length of password

first query i try like: `select id from prob_orc where id='admin' and pw='' or id='admin' and length(pw)=8#'` so payload of `?pw= ' or id='admin' and length(pw)=1#'`

2 signal for me to check true - false length is web server will return `admin` if true query.

[Check length password script](scripting/l4.py)

Using this I know length of password is `8`

Let's substr() to extract one by one data

`' or id = 'admin' and ascii(substr(pw,1,1)) = 48 #` throw `hello admin`, so, let write a script to brute force this

[Exploted](scripting/l4.py)

Payload: `' or id = 'admin' and ascii(substr(pw,1,1)) = 48 #`