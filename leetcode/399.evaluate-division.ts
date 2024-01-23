function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    var graph : {[key:string] : [string,number][] } = {} 

    // make graph
    for (let elem = 0; elem < equations.length; elem++) {
        if (graph[equations[elem][0]] == undefined) {
            graph[equations[elem][0]] = []
        }
        if (graph[equations[elem][1]] == undefined) {
            graph[equations[elem][1]] = []
        }

        graph[equations[elem][0]].push([equations[elem][1], values[elem]])
        graph[equations[elem][1]].push([equations[elem][0], 1 / values[elem]])
    }

    var out: number[] = []

    // dfs
    for (const query of queries) {
        
        if (graph[query[0]] == undefined) {
            out.push(-1)
            continue
        }

        let queue: [string, number][] = [[query[0], 1]] 
        let visited = new Set()
        let found = false

        while (queue.length != 0) {
            let elem = queue.pop() as [string,number]
            if (visited.has(elem[0])) {
                continue
            }
            visited.add(elem[0])

            if (elem[0] == query[1]) {
                out.push( elem[1] )
                found = true
                break
            }
            for (const link of graph[elem[0]]) {

               queue.push([link[0],elem[1] * link[1]]) 
            }
        }
        if (!found) {
            out.push(-1)
        }
    }
    return out

};