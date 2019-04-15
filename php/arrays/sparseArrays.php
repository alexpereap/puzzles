<?php

function matchingStrings($strings, $queries){
    $r = [];
    
    foreach( $queries as $q ){
        $m = 0;
        foreach( $strings as $s ){
            if( $s == $q )
                $m += 1;
        }
        $r[] = $m;
    }

    return $r;
}

$strings = ['aba', 'baba', 'aba', 'xzxb'];
$queries = ['aba', 'xzxb', 'ab'];

print_r(matchingStrings($strings, $queries));