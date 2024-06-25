import ply.lex as lex
import ply.yacc as yacc
from lexico import create_lexer
from semantico import create_parser

def check_code(content, token_table, result_table, error_table):
    lexer, tokens = create_lexer(error_table)
    parser, result_table, error_table = create_parser(error_table, result_table, tokens)
    # Use the lexer to tokenize the input content
    lexer.input(content)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_table.append(f"{tok.type}: {tok.value}")
    # Use the parser to parse the content
    while True:
        tok = parser.parse(content)
        if not tok:
            break
        result_table.append(f"{tok.type}: {tok.value}")
    return tokens, error_table, result_table
