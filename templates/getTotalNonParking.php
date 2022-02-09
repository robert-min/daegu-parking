<?php
    header("Content-Type:application/json");
    header("Access-Control-Allow-Origin: *");


    // 1. 데이터베이스에서 데이터를 가져옴
    $link = mysqli_connect("localhost", "root", "aksen5466!", "parking");
    if ($result = mysqli_query($link, 'SELECT * FROM `illegal` WHERE count >= 2;', MYSQLI_USE_RESULT)) {
        // 2. 데이터베이스로부터 반환된 데이터를
        // 객체 형태로 가공함
        $o = array();
        while ($row = mysqli_fetch_object($result)) {
            $t = new stdClass();
            $t->id = $row->id;
            $t->address = $row->address;
            $t->count = $row->count;
            $t->year = $row->year;
            $t->lat = $row->lat;
            $t->lng = $row->lng;
            $o[] = $t;
            unset($t);
        }
    } else {
        $o = array( 0 => 'empty');
    }

    // 3, 4 최종 결과 데이터를 JSON 스트링으로 변환 후 출력
    echo json_encode($o);