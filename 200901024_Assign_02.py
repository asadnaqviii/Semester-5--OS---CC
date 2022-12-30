import re   # Regex library
import ast  # Abstract Syntax Tree library

# defines regular expressions for different types of tokens
number_regex = r'\d+(\.\d+)?'  # to match integers and floating point numbers
operator_regex = r'[+-/*()]'   # to match basic arithmetic operators and parentheses
identifier_regex = r'[a-zA-Z_][a-zA-Z0-9_]*'  # for matching identifiers

def tokenize(expression):
  # extract the tokens from the input string using regular expressions
  numbers = re.findall(number_regex, expression)
  operators = re.findall(operator_regex, expression)
  identifiers = re.findall(identifier_regex, expression)

  # combine the numbers, operators, and identifiers into a single list of tokens
  tokens = []
  for number in numbers:
    tokens.append(number)
  for operator in operators:
    tokens.append(operator)
  for identifier in identifiers:
    tokens.append(identifier)

  print(tokens)
  return tokens

# run the tokenizer by entering expression
expression = 'a + (b * c)'
tokens = tokenize(expression)
print(tokens)
  
tree = ast.parse(expression)   # Parse the input expression by takeing a string containing a Python expression, and returns an AST object representing the parsed expression.
print(ast.dump(tree))    # Use this function to print the abstract syntax tree in a human understandable form

# Using a node visiter class (optional)
class TreeVisitor(ast.NodeVisitor):
  def visit_Name(self, node):
    print(f'Node type: {type(node).__name__}, Node value: {node.id}')
  def visit_BinOp(self, node):
    print(f'Node type: {type(node).__name__}, Node value: {node.op.__class__.__name__}')

def build_syntax_tree(expression):
  tree = ast.parse(expression)
  visitor = TreeVisitor()
  visitor.visit(tree)
  
build_syntax_tree(expression)  # Generates Syntax tree of given expression
