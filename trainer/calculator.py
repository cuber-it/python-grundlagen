#!/usr/bin/env python3
import argparse
import operator
import sys

# Mapping der unterstützten Operatoren
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow
}

def main():
    parser = argparse.ArgumentParser(description='Ein einfacher Taschenrechner für arithmetische Operationen.')

    # Operanden und Operator als Argumente
    parser.add_argument('operand1', type=float, help='Erster Operand (Zahl)')
    parser.add_argument('operator', choices=OPERATIONS.keys(), help='Operator (+, -, *, /, //, %, **)')
    parser.add_argument('operand2', type=float, help='Zweiter Operand (Zahl)')

    args = parser.parse_args()

    # Ausführung der Operation
    try:
        result = OPERATIONS[args.operator](args.operand1, args.operand2)
        print(f'{args.operand1} {args.operator} {args.operand2} = {result}')
    except ZeroDivisionError:
        print('Fehler: Division durch Null ist nicht erlaubt.', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
