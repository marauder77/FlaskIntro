from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)


def add(a, b):
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    
    return str(result)

def sub(a, b):
    """Substract b from a."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    
    return str(result)

def mult(a, b):
    """Multiply a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


def div(a, b):
    """Divide a by b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    
    return str(result)