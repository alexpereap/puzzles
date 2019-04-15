minimumSwaps = arr =>{
    let goal = [...arr];
    goal.sort();
    let numSwaps = 0;

    goal.forEach((v,k)=>{
        if(v != arr[k]){
            let idx = arr.indexOf(v);
            let old_value = arr[k];
            
            arr[k] = v;
            arr[idx] = old_value;
            numSwaps++;
        }
    });

    return numSwaps;
};

arr = [1,3,5,2,4,6,7];
console.log(minimumSwaps(arr));