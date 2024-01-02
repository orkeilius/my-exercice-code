function findMatrix(nums: number[]): number[][] {
  var hash :Record<number,number> = {}
  
  var matrix :number[][] = []

  for (const elem of nums){
    if (!(elem in hash)){
      hash[elem] = -1
    }
    hash[elem] ++

    if (matrix.length == hash[elem] ){
        matrix.push([])
    }

    matrix[hash[elem]].push(elem)
  }

  return matrix
};
