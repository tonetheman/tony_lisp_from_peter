
import sys

class Symbol(str):
    pass

def Sym(s, symbol_table={}):
    if s not in symbol_table:
        symbol_table[s] = Symbol(s)
    return symbol_table[s]

_quote, _if, _set, _define, _lambda, _begin, _definemacro = map(Sym,
    "quote if, set! define lambda begin define-macro".split())

_quasiquote, _unquote, _unquotesplicing = map(Sym,
    "quasiquote unquote unquote-splicing".split())

class InPort(object):
    tokenizer = r'''\s*(,@|[('`,)]|"(?:[\\].|[^\\"])*"|;.*|[^\s('"`,;)]*)(.*)'''
    def __init__(self,file):
        self.file = file
        self.line = ""
    def next_token(self):
        while True:
            if self.line == "":
                self.line = self.file.readline()
            if self.line == "":
                return eof_object
            token, self.line = re.match(InPort.tokenizer,self.line).groups()
            if token != "" and not token.startswith(";"):
                return token

eof_object = Symbol('#<eof-object>') # Note: uninterned; can't be rea

# TODO: not done
def read(inport):
    def read_ahead(token):
        pass

quotes = { "`" : _quasiquote, "'" : _quote, ",":_unquote, ",@":_unquotesplicing}

# TODO: not done
def atom(token):
    pass

# TODO: not done
def to_string(x):
    if x is True:
        return "#t"
    elif x is False:
        return "#f"
    elif isa(x, Symbol):
        return x


def repl(prompt=">tlisp> ", inport=InPort(sys.stdin), out=sys.stdout):
    sys.stderr.write("tlisp version 0\n")
    while True:
        try:
            if prompt:
                sys.stderr.write(prompt)
        except Exception as e:
            print "%s : %s" % (type(e).__name__, e)



