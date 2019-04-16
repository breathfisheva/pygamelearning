#列出列表的全排列
# result = []
def list_result(l, s='', result=[]):
    for index, item in enumerate(l):
        rest_list = l[:index] + l[index+1:]
        pickdata = s+item
        if rest_list == []:
            result.append(pickdata)
        list_result(rest_list, pickdata, result)

    return result

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def one_expression_tree(operators, operands):
    root_node = Node(operators[0])
    operator1 = Node(operators[1])
    operator2 = Node(operators[2])
    operand0 = Node(operands[0])
    operand1 = Node(operands[1])
    operand2 = Node(operands[2])
    operand3 = Node(operands[3])
    root_node.left = operator1
    root_node.right =operand0
    operator1.left = operator2
    operator1.right = operand1
    operator2.left = operand2
    operator2.right = operand3
    return root_node

def two_expression_tree(operators, operands):
    root_node = Node(operators[0])
    operator1 = Node(operators[1])
    operator2 = Node(operators[2])
    operand0 = Node(operands[0])
    operand1 = Node(operands[1])
    operand2 = Node(operands[2])
    operand3 = Node(operands[3])
    root_node.left = operator1
    root_node.right =operator2
    operator1.left = operand0
    operator1.right = operand1
    operator2.left = operand2
    operator2.right = operand3
    return root_node

def cal(a, b, operator):
    return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '÷' and float(a)/float(b)

def cal_tree(node):
    if node.left is None:
        return node.val
    return cal(cal_tree(node.left), cal_tree(node.right), node.val)

def print_expression_tree(root):
    print_node(root)
    print (' = 24')

def print_node(node):
    if node is None :
        return
    if node.left is None and node.right is None:
        print (node.val,end='')
    else:
        print ('(', end='')
        print_node(node.left)
        print (node.val,end='')
        print_node(node.right)
        print (')',end='')

def calculate(nums):
    nums_possible = list_result(nums)
    operators_possible = list_result(['+','-','*','÷'], result=[]) #这里有一个问题，如果不设置result为空，operators_possible和  nums_possible  结果会混在一起
    goods_noods = []
    for nums in nums_possible:
        for op in operators_possible:
            node = one_expression_tree(op, nums)
            if cal_tree(node) == 24:
                goods_noods.append(node)
            node = two_expression_tree(op, nums)
            if cal_tree(node) == 24:
                goods_noods.append(node)

    for node in goods_noods:
        print_expression_tree(node)


calculate(['1', '2', '3', '8'])

# if __name__ == '__main__':
#     l = ['1', '2', '3']
#     print(list_result(l))
