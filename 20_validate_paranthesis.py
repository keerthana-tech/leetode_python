class Solution:
    def isValid(self, s: str) -> bool:
        hadict={ ")" : "(" , "}" : "{" , "]" : "[" }
        st=[]
        
        
        for i in s:
            if i in hadict:
                top = st.pop() if st else "#"
                
                if hadict[i]!=top:
                    return False
            else:
                st.append(i)
                
        return len(st)==0
