class User {
        private $role;

        function __construct($role) {
            $this->role = $role;
        }

        function __wakeup() {
            if (isset($this->role)) eval($this->role);
        }
    }

$user_data = unserialize($_COOKIE['data']);
