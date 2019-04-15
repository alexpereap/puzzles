countingValleys = (n, s)=>{
    if(!(2 <= n && n <= Math.pow(10, 6)))
        return 0;
    
    let level = 0;
    let in_valley = false;
    let eneterd_valley = 0;

    s.split("").forEach(direction => {
        if(direction == 'U')
            level += 1;
        else if(direction == 'D')
            level -= 1;
        else
            return 0;
        
        if(!in_valley && level < 0){
            in_valley = true;
            eneterd_valley += 1;
        } else if(in_valley && level == 0)
            in_valley = false;
    });

    console.log(eneterd_valley);
}

countingValleys(8, 'UDDDUDUU')
countingValleys(8, 'UDDDUDUUUUDDDUUUDDDDUDUU')