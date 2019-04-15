<?php

function repeatedString($s, $n){
    $l = strlen($s);
    $q = intdiv($n, $l);
    $r = $n % $l;
    $a = 0;
    
    foreach(str_split($s) as $c){
        if($c == 'a')
        $a += 1;
    }
    
    $total = $a * $q;
    
    if( $r > 0 ){
        foreach( range(1, $r) as $key => $x ){

            if($s[$key] == 'a')
                $total += 1;
        }
    }
    
    return $total;
}

print(repeatedString('a', 1000000000000));

// aba aba aba a