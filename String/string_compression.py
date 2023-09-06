class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) == 1:
            return 1
        
        currChar = chars[0]
        counter = 1
        output = 0
        index = 0

        for i in range(1, len(chars)):

            if chars[i] == currChar and i < len(chars)-1:
                counter += 1

            elif chars[i] == currChar and i == len(chars)-1:
                counter += 1
                chars[index] = currChar

                if counter > 1:
                    l = len(str(counter))
                    for j in range(l):
                        chars[index+1+j] = str(counter)[j]
                    output += l
                
                output += 1

            elif chars[i] != currChar:

                chars[index] = currChar
                if counter > 1:
                    l = len(str(counter))
                    for j in range(l):
                        chars[index+1+j] = str(counter)[j]
                    output += l
                    index += l

                output += 1
                index += 1
                currChar = chars[i]
                counter = 1

                if i == len(chars)-1:
                    output += 1
                    chars[index] = currChar

        return output

