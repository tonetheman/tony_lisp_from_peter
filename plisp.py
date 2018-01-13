

import math
import operator as op


Symbol = str
Number = (int,float)
Atom = (Symbol,Number)
List = list
Exp = (Atom,List)
Env = dict


def standard_env():
    env = Env()
    env.update(vars(math))
    return env

def tokenize(s):
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens):
    if len(tokens)==0:
        raise SyntaxError("unexpected EOF")
    token = tokens.pop()
    if token =="(":
        L = []
        while tokens[0] != ")":
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ")":
        raise SyntaxError("unexpected )")
    else:
        return atom(token)

def parse(s):
    return read_from_tokens(tokenize(s))

def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)

def eval(x, env):
    if isinstance(x,Symbol):
        return env[x]
    elif not isinstance(x,Number):
        return x
    elif x[0] == "if":
        (_,test,conseq,alt)=x
        exp = (conseq if eval(test,env) else alt)
        return eval(exp,env)
    elif x[0] == "define":
        (_,symbol,exp) = x
        env[symbol] = eval(exp,env)
    else:
        proc = eval(x[0],env)
        args = [eval(arg,env) for arg in x[1:]]
        return proc(*args)



eval(parse("(begin (define r 10) (* pi (* r r)))"))
