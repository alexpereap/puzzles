<?php

function reverseString($s){
    $s = str_split($s);
    $r = [];
    for($i = count($s) - 1; $i>= 0; $i-- ){
        $r[] = $s[$i];
    }

    // print_r($r);
    for($i = count($s) - 1; $i>=0; $i--){
        $r[$i] = $s[ (count($s) -1) - $i ];
    }

    print_r($r);
}

$s = 'aeiou';
reverseString($s);