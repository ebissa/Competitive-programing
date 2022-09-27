class Solution:
    def isValid(self, s: str) -> bool:
        openSymbols=[]
        for symbol in s:
            if symbol in["(","{","["]:
                openSymbols.append(symbol)
            elif symbol in[")","}","]"] and len(openSymbols)!=0:
                if symbol==")" and openSymbols[len(openSymbols)-1]=="(":
                    openSymbols.pop()
                elif symbol=="]" and openSymbols[len(openSymbols)-1]=="[":
                    openSymbols.pop()
                elif symbol=="}" and openSymbols[len(openSymbols)-1]=="{":
                    openSymbols.pop()
                else:
                    return False
            else:return False
        if openSymbols==[]:
            return True
