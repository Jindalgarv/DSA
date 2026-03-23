class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    arr.append(board[i][j])
            if self.containsNoDuplicate(arr)== False:
                return False
            arr.clear()
        for i in range(9):
            for j in range(9):
                if board[j][i]!=".":
                    arr.append(board[j][i])
            if self.containsNoDuplicate(arr)== False:
                return False
            arr.clear()
        
        for a in range(0,7,3):
            for b in range(0,7,3):
                for i in range(a,3+a):
                    for j in range(b,3+b):
                        if board[i][j]!=".":
                            arr.append(board[i][j])
                if self.containsNoDuplicate(arr)== False:
                    return False
                arr.clear()
        return True

    def containsNoDuplicate(self,arr:list[str])->bool:

        return len(arr)==len(set(arr))

        