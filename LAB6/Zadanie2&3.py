def balans(str):
stos = []
index = 0
while index < len(str):
            	symbol = str[index]
            	if symbol == '(':
            		stos.append(symbol)
        		else:
            		if symbol == ')':
                			if not stack:
                    				return False
                			else:
                    				stos.pop()
       		 index += 1
    	return not stos

str1 = '((()))()'
print(balans(str1))     #True

str2 = '((())()'
print(balans(str2))   #False
