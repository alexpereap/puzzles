repeatedString = (s,n) =>{
    let l = s.length;
    let q = Math.floor(n/l)
    let r = n % l;
    let a = 0;

    // get numer of a
    s.split("").forEach(c =>{
        if(c == 'a')
            a += 1;
    });

    total = a * q;

    // range(0,r)
    [...Array(r).keys()].forEach( x =>{
        if(s[x] == 'a')
            total += 1;
    });

    return total;
}

r = repeatedString('a', 100000000);
console.log(r);