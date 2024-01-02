function checkStrings(s1: string, s2: string): boolean { 
    let frequency1 = getFrequency(s1) 
    let frequency2 = getFrequency(s2)

    for (let i = 0; i < 51; i++) {
        if (frequency1[i] != frequency2[i]) {
            return false
        }       
    }
    return true
};

function getFrequency(str: string): object{ //
    var frequency:object = Array(51).fill(0)
    
    for (let i = 0; i < str.length; i++) {
        frequency[str.charCodeAt(i) - 97 + (i%2 * 26)] ++;
        
    }
    console.log(frequency)
    return frequency
}