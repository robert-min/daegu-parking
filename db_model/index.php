<?php

require_once('db.php');

$db = new MysqliDb ('localhost', 'root', 'aksen5466!', 'parking');

$users = $db->get('illegal'); //contains an Array of all users

print_r($users);
