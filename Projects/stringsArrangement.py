def stringsRearrangement(inputArray):
    for i in range(len(inputArray) - 1):
        c = 0
        for j in range(len(inputArray[0])):
            if inputArray[i][j] != inputArray[i+1][j]: c += 1
        if c != 1: return False

    return True
            



inp = ["ab", "bb", "aa"]
print(stringsRearrangement(inp))

# function stringsRearrangement(inputArray) {
#     var ret = false;
#     var solution = [];
    
#     function bt () {
#         for (var i = 0; i<inputArray.length; i++) {
#             if(ret) break;
#             solution.push(inputArray.splice(i,1)[0]);
#             if (inputArray.length === 0) {
#                 ret = ret || checkSolution();
#             }
#             else{
#                 bt();
#             }
#             inputArray.splice(i,0,solution.pop());
#         }
        
#     }
#     function checkSolution () {
#         for (var i = 0; i < solution.length - 1; i++){
#             var diff =0;
#             for (var j = 0; j<solution[i].length; j++) {
#                 if (solution[i][j] !== solution[i+1][j]){
#                     diff++;
#                 }
#             }
#             if(diff !== 1){
#                 return false;
#             }
#         }
#         return true;
#     }
#     bt();
#     return ret;
# }