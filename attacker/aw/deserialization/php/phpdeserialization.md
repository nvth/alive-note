## Ví dụ deserialization `demo-oop.php`

đoạn chuỗi trả về dạng

O:LENTH_OF_NAME:"CLASS_NAME":NUMBER_OF_PROPERTIES:{PROPERTIES}

## Cách phát hiện :

có sử dụng hàm gọi tự động không cần hàm khác gọi tới, magic method `__wakeup()` hoặc `__detruct()` 

bao gồm các hàm có ký tự `__funcname` trước hàm

```php
__construct(), __destruct(), __call(), __callStatic(), __get(), __set(), __isset(), __unset(), __sleep(), __wakeup(), __serialize(), __unserialize(), __toString(), __invoke(), __set_state(), __clone(), __debugInfo()
```

