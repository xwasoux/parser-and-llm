import ipdb
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser

input_stream = InputStream("hello parrt")
lexer = HelloLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = HelloParser(stream)
tree = parser.r()
# ipdb.set_trace()
print(tree.toStringTree(recog=parser))
