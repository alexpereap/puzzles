<?php

function minimumSwaps($arr){

    $min = null;

    $goal = $arr;
    sort($goal);
    $numSwaps = 0;

    foreach($goal as $k => $v){
        if( $v != $arr[$k] ){
            $idx = array_search($v, $arr);
            $old_value = $arr[$k];
            $arr[$k] = $v;
            $arr[$idx] = $old_value;
            $numSwaps++;
        }
    }

    return $numSwaps;
    
}

$arr = [1,3,5,2,4,6,7];
// 1,2,5,3,4,6,7

// 1,2,3,5,4,6,7
// 1,2,3,4,5,6,7

minimumSwaps($arr);