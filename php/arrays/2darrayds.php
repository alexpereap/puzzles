<?php

function hourglassSum($arr){
    $total = null;

    // offsets
    $left = 0;
    $right = 3;
    $middle =  1;
    $row = 0;

    // $initalSubset = array_slice($arr[$row], $left ,$right);
    // $initalSubset[] = $arr[$row + 1][$middle];
    // $initalSubset = array_merge($initalSubset, array_slice($arr[$row + 2], $left, $right));

    // var_dump($initalSubset);
    // var_dump(array_sum($initalSubset));

    for($i = 1; $i <= 16; $i++){
        $initalSubset = array_slice($arr[$row], $left ,3);
        $initalSubset[] = $arr[$row + 1][$middle];
        $initalSubset = array_merge($initalSubset, array_slice($arr[$row + 2], $left, 3));

        $temp_total = array_sum($initalSubset);

        if($temp_total > $total || is_null($total) )
            $total = $temp_total;
        
        $left +=1;
        $right +=1;
        $middle += 1;

        if( $i % 4 == 0 ){
            $row +=1;
            $left = 0;
            $right = 3;
            $middle =  1;
        }
    }

    return $total;
}

$array = array(
    [1 ,1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
);

$array = array(
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
);

$array = array(
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
);

$array = array(
    [-1, 1, -1, 0, 0, 0],
    [0, -1, 0, 0, 0, 0],
    [-1, -1, -1, 0, 0, 0],
    [0, -9, 2, -4, -4, 0],
    [-7, 0, 0, -2, 0, 0],
    [0, 0, -1, -2, -4, 0]
);

print(hourglassSum($array));