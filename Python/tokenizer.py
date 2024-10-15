#!/usr/bin/env python
# coding: utf-8

# In[1]:


##------------------------FUNCTION: To convert an expression into a list of tokens ------------------------##
def tokenizer(expression:str)-> list:
    number_status = False
    token = ""
    list_of_tokens = []
    # operators and parnetehesis
    operators = ["+", "-", "^", "*", "/", "(", ")"]
    
    for index, char in enumerate(expression):
        if char in operators:
            if number_status == True:
                list_of_tokens.append(token)
                token = ""
                number_status = False
            list_of_tokens.append(char)
        # if a number
        elif char.isnumeric() == True:
            number_status = True
            token = token + char
            # if the last element of expression
            if index == len(expression)-1:
                list_of_tokens.append(token)
        else:
            pass
    return list_of_tokens

##------------------------FUNCTION: To highlight unary symbols within a token ------------------------##
def unaryTokenizer(list_of_token:list)->list:
    first_status = True
    operator_status = False
    # operators and parnetehesis
    operators = ["+", "-", "^", "*", "/", "(", ")"]
    
    for index, token in enumerate(list_of_token):
        if index > 0:
            first_status = False
        if token in operators:
            if token in ["+", "-"] and (first_status == True or operator_status == True):
                modified_token = "u" + token
                list_of_token[index] = modified_token
            else:
                operator_status = True
        else:
            operator_status = False
    return list_of_token

##------------------------FUNCTION: To convert infix expression to postfix token ------------------------##
def postfixTokenizer(expression:str)->list:
    operators:list = []
    postfix = []
    operatorsSymbols = ["+", "-", "^", "*", "/", "u-", "u+"]
    
    non_unary_infix = tokenizer(expression)
    infix = unaryTokenizer(non_unary_infix)
    for index, token in enumerate(infix):
        if token.isnumeric() == True:
            postfix.append(token)
        elif token in operatorsSymbols:
            while len(operators) != 0 and operators[len(operators)-1] != "(":
                last_item = operators.pop()
                postfix.append(last_item)
            operators.append(token)
        elif token == "(":
            operators.append(token)
        else:
            while len(operators) != 0 and operators[len(operators)-1] != "(":
                last_item = operators.pop()
                postfix.append(last_item)
            operators.remove("(")
    while len(operators) != 0:
        last_item = operators.pop()
        postfix.append(last_item)
    return postfix

##------------------------FUNCTION: To evlaute a postfix expression------------------------##
def evaluatePostFix(list_of_token:list)->float or int:
    values = []
    unary = ["u-", "u+"]
    binary = ["+", "-", "^", "*", "/"]
    
    for index, token in enumerate(list_of_token):
        if token.isnumeric() == True:
            values.append(int(token))
        elif token in unary:
            lastItem = values.pop()
            if token == "u-":
                lastItem = lastItem * -1
            values.append(lastItem)
        elif token in binary:
            left = values.pop()
            right = values.pop()
            if token == "+":
                computation = right + left
            elif token == "-":
                computation = right - left
            elif token == "^":
                computation = right ^ left
            elif token == "*":
                computation = right * left
            else:
                computation = right / left
            values.append(computation)
        else:
            raise ValueError("Invalid token")
    return values

def main()-> None:
    string = input("Enter mathematical expression: ")
    expression = postfixTokenizer(string)
    print(expression)
    result = evaluatePostFix(expression)
    print(result)
main()


# In[ ]:




