def is_valid_post_format(post):
    stack = []
    matching_tags = {')': '(', ']': '[', '}': '{'}
    
    for char in post:
        if char in matching_tags.values():  
            stack.append(char)
        elif char in matching_tags:  
            if not stack or stack.pop() != matching_tags[char]:  
                return False 
    
    return len(stack) == 0  

print(is_valid_post_format("()"))      
print(is_valid_post_format("()[]{}"))  
print(is_valid_post_format("(]"))   