import ply.yacc as yacc

def create_parser(result_table, error_table, tokens):
    declared_variables = set()

    def p_init(p):
        '''init : include function'''
        
    def p_include(p):
        '''include : GATO INCLUDE OPLOG ID OPLOG'''

    def p_function(p):
        '''function : INT MAIN PAREI PARED BRACI statement_list BRACD'''
        result_table.append("Función main correctamente estructurada")

    def p_statement_list(p):
        '''statement_list : statement statement_list
                          | statement'''

    def p_statement(p):
        '''statement : variable_declaration
                     | assignment
                     | for_loop
                     | return_statement'''

    def p_variable_declaration(p):
        '''variable_declaration : INT var_list PUNTOCOMA'''
        for var_name in p[2]:
            if not var_name.isidentifier() or not var_name[0].isalpha():
                error_table.append(f"Error: Identificador '{var_name}' no válido en la línea {p.lineno(2)}")
            elif var_name in declared_variables:
                error_table.append(f"Error: Variable '{var_name}' redeclarada en la línea {p.lineno(2)}")
            else:
                declared_variables.add(var_name)
                result_table.append(f"Variable '{var_name}' declarada")

    def p_var_list(p):
        '''var_list : ID
                    | ID IGUAL expression
                    | var_list COMA ID
                    | var_list COMA ID IGUAL expression'''
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4 and p[2] == '=':
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = p[1] + [p[3]]
        elif len(p) == 6:
            p[0] = p[1] + [p[3]]

    def p_assignment(p):
        '''assignment : INT ID IGUAL expression PUNTOCOMA
                    | ID IGUAL expression PUNTOCOMA'''
        var_name = p[1]
        if var_name not in declared_variables:
            error_table.append(f"Error: Variable '{var_name}' no declarada antes de su uso en la línea {p.lineno(1)}")
        else:
            result_table.append(f"Variable '{var_name}' asignada")

    def p_expression(p):
        '''expression : term
                      | expression OPMAT term'''

    def p_term(p):
        '''term : NUM
                | ID'''
        if isinstance(p[1], str) and p[1] not in declared_variables:
            error_table.append(f"Error: Variable '{p[1]}' no declarada antes de su uso en la línea {p.lineno(1)}")

    def p_for_loop(p):
        '''for_loop : FOR PAREI ID IGUAL NUM PUNTOCOMA ID OPLOG NUM PUNTOCOMA ID OPMAT PARED BRACI statement_list BRACD'''
        var_name1 = p[3]
        var_name2 = p[7]
        var_name3 = p[11]
        if var_name1 != var_name2 or var_name2 != var_name3 or var_name1 != var_name3:
            error_table.append("Error en los ID de la estructura for")
        elif var_name1 not in declared_variables:
            error_table.append(f"Error: Variable '{var_name1}' no declarada antes de su uso en for")
        else:
            result_table.append("For correctamente estructurado")

    def p_condition(p):
        '''condition : expression OPLOG expression'''
        
    def p_return_statement(p):
        '''return_statement : RETURN NUM PUNTOCOMA
                            | RETURN ID PUNTOCOMA'''
        if isinstance(p[2], str) and p[2] not in declared_variables:
            error_table.append(f"Error: Variable '{p[2]}' no declarada antes de su uso en la línea {p.lineno(2)}")

    def p_error(p):
        if p:
            error_table.append(f"Error: Unexpected token '{p.value}' at line {p.lineno}, position {p.lexpos}")
        else:
            error_table.append("Error: Syntax error at EOF")

    parser = yacc.yacc()
    return parser, result_table, error_table