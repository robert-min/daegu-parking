<?php
    header("Content-Type: application/json");

    require_once('db.php');

    $db = new MysqliDb ('localhost', 'root', 'aksen5466!', 'parking');

    $list = $db->get('illegal', 100);

    echo json_encode($list);
