rotLeft = (a, d) =>{
    let b = [...a];
    
    [...Array(a.length).keys()].forEach(i=>{
        let index = (i + d) % a.length;
        b[i] = a[index];
    });

    return b;
};

console.log(rotLeft([1, 2, 3, 4, 5,], 4));