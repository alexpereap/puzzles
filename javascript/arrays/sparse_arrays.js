matchingStrings = (strings, queries) =>{
    let r = [];
    queries.forEach(q=>{
        let m = 0;
        strings.forEach(s=>{
            if(s==q)
                m++
        })
        r.push(m);
    });

    return r;
}

strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']

console.log(matchingStrings(strings, queries))