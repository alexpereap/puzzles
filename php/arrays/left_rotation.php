<?php

function rotLeft($a, $d){
    
    for($i = 0; $i < count($a); $i++){
        $index = ($i + $d ) % count($a);
        $b[$i] = $a[$index];
    }
    
    return $b;
}

var_dump(rotLeft([1, 2, 3, 4, 5,], 4));