class Solution:
    # Algo: Add length<delimiter>string as a single string and then
    # decode 
    def encode(self, strs: List[str]) -> str:
        encode = []
        for s in strs:
            n = len(s)
            encode.append(str(n))
            encode.append('#')
            encode.append(s)
        return "".join(encode)


    # use 2 pointers, one for the starting where the length size starts 
    # and the other for the ending. 
    # Then skip delimiter and take char size as found and move on
    def decode(self, s: str) -> List[str]:
        decode = []
        n = len(s)
        i = 0 # start
        while(i < n):
            j = i
            while(s[j] != '#'):
                j = j+1
            size = int(s[i:j])
            decode.append(s[j+1:j+1+size])
            i = j + 1 + size # move i to j(end)
        return decode
