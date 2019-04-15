jumpingOnClouds = c =>{
    let jumps  = 0;
    let i = 0;

    while(i < c.length - 1 ){
        if((i+2) < c.length && c[i+2] != 1){
            i += 1;
        }

        jumps += 1;
        i += 1;
    }

    console.log(jumps);
    return jumps;
}

jumpingOnClouds([0, 0, 0, 1, 0, 0]) //  3
jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) //  4
jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]) //  3
jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0]) // 6