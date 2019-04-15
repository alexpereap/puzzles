hourglassSum = arr => {
    let total = null;

    let left = 0;
    let right = 3;
    let middle = 1;
    let row = 0;

    [...Array(16).keys()].forEach(idx => {
        let i = idx +1;
        let initialSubset = arr[row].slice(left, right)
        
        initialSubset.push(arr[row+1][middle])
        initialSubset = initialSubset.concat(arr[row+2].slice(left, right))

        let temp_total = initialSubset.reduce( (a, b)=>{
            return a + b;
        },0);

        if(total == null){
            total = temp_total;
        } else if(temp_total > total){
            total = temp_total;
        }

        left += 1
        right += 1
        middle += 1

        if(i % 4 == 0){
            row += 1
            left = 0
            right = 3
            middle = 1
        }
    });

    return total;
};

array = [
    [1 ,1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

console.log(hourglassSum(array));