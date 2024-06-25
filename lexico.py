import ply.lex as lex
import tkinter as tk


def create_lexer(error_table):
    # Define reserved words
    error_table = []
    reserved = {
        "int": "INT",
        "return": "RETURN",
        "for": "FOR",
        "main": "MAIN",
        "include" : "INCLUDE",
        "string": "STRING"
    }

    tokens = [
        "PAREI",
        "PARED",
        "IGUAL",
        "OPMAT",
        "OPLOG",
        "PUNTOCOMA",
        "BRACI",
        "BRACD",
        "ID",
        "NUM",
        "NEWLINE",
        "GATO",
        "COMA",
    ] + list(reserved.values())

    t_PAREI = r"\("
    t_PARED = r"\)"
    t_IGUAL = r"="
    t_OPMAT = r"(\+|\-|\*|\/)"
    t_OPLOG = r"(>=|<=|==|!=|>|<)"
    t_PUNTOCOMA = r";"
    t_BRACI = r"\{"
    t_BRACD = r"\}"
    t_GATO = r"\#"
    t_COMA =r","
    
    def t_ID(t):
        r"[a-zA-Z_][a-zA-Z_0-9]*(\.[a-zA-Z_0-9]+)?"
        t.type = reserved.get(t.value, "ID")
        return t
    
    def t_NUM(t):
        r"\d+"
        t.value = int(t.value)
        return t
    
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = " \t\r"

    def t_error(t):
        error_table.append("caracter no valido")
        t.lexer.skip(1)

    lexer = lex.lex()
    return lexer, tokens
