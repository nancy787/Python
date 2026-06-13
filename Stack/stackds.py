#  infix expression to a postfix expression.
def priority(operator) :
    priority = -1
    if operator == '^' :
        priority = 3
    elif operator =='*' or operator == '/':
        priority = 2
    elif operator =='+' or operator == '-':
        priority = 1

    return priority

def infixToPostfix(s):
    i = 0
    st = []
    ans = ''

    while i < len(s):

        if s[i] == ' ':      # skip spaces
            i += 1
            continue

        if s[i].isalnum():
            ans += s[i]

        elif s[i] == '(':
            st.append(s[i])

        elif s[i] == ')':
            while st and st[-1] != '(':
                ans += st.pop()
            st.pop()

        else:
            while st and priority(s[i]) <= priority(st[-1]):
                ans += st.pop()
            st.append(s[i])

        i += 1

    while st:
        ans += st.pop()

    return ans

res = infixToPostfix('a + b * (c^d - e) ^ (f + g * h) - i')
print('Infix to postfix', res)