sockMerchant = (n, ar) => {
    let total_pairs = 0;

    if(n < 2)
        return 0;

    let ar2 = [];
    
    ar.forEach((col, idx) =>{
        let pairs = 0;
        let ar3 = [];

        if(idx == 0){
            ar2 = ar;
        }

        ar2.forEach((col2, idx2)=>{
            if(col == col2){
                pairs += 1;
            }else{
                ar3.push(col2);
            }
        });

        ar2 = ar3;
        total_pairs = total_pairs + Math.floor(pairs/2)
    });

    return total_pairs;
}
r = sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
console.log(r);