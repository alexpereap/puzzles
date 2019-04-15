<?php

function countingValleys($n, $s){
    if( !( 2 <= $n && $n <= pow(10, 6) ) )
        return 0;

    $s = str_split($s);

    $level = 0;
    $in_valley = false;
    $entered_valley = 0;

    foreach( $s as $direction ){
        if( $direction == 'U' ){
            $level += 1;
        } else if($direction == 'D'){
            $level = $level -= 1;
        } else{
            return 0;
        }

        if( !$in_valley && $level < 0 ){
            $in_valley = true;
            $entered_valley += 1;
        } else if($in_valley && $level == 0){
            $in_valley = false;
        }
    }

    print($entered_valley . "\n");
}
countingValleys(8, 'UDDDUDUU');
countingValleys(8, 'UDDDUDUUUUDDDUUUDDDDUDUU');