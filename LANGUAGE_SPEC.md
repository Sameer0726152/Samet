# Samet Language Specification

> **Status:** Work in Progress  
> **Implementation:** Python interpreter  
> **Current focus:** Core syntax, expressions, variables, and basic control flow

Samet is a small experimental programming language built from scratch to explore how programming languages work internally.

The current implementation follows this pipeline:

```text
Samet Source Code
       ↓
     Lexer
       ↓
     Tokens
       ↓
     Parser
       ↓
      AST
       ↓
  Interpreter
       ↓
 Runtime Environment
       ↓
     Output
```

This document defines the syntax and behavior currently intended for Samet. Features marked as planned are not yet part of the implemented language.

---

## 1. Design Goals

Samet is being developed with the following goals:

- Simple and readable syntax
- Explicit basic data types
- A custom lexer and parser
- An Abstract Syntax Tree (AST)
- A tree-walking interpreter
- Clear language rules and error behavior
- Educational value: understanding how a programming language is built from scratch

Samet is currently **interpreted**, not compiled to machine code.

The interpreter itself is implemented in Python.

---

# 2. Basic Syntax Rules

## 2.1 Statement termination

Every Samet statement ends with:

```text
\
```

Example:

```text
num Age = 20\
write<Age>\
```

A statement that requires termination but does not contain `\` is invalid.

---

## 2.2 Comments

Comments begin with `#` and continue until the end of the line.

Example:

```text
# This is a comment
num Age = 20\
```

Comments are ignored by the lexer.

---

## 2.3 Case sensitivity

Samet is case-sensitive.

These are different identifiers:

```text
Age
age
AGE
```

However, identifiers must follow Samet's identifier rules described below.

---

# 3. Identifiers

Identifiers are names used for variables.

## Rules

A Samet identifier:

1. Must begin with an uppercase English letter.
2. May contain letters.
3. May contain digits after the first character.
4. May contain `_`.
5. Is case-sensitive.

Valid:

```text
Age
Student
Student1
My_Value
X
TotalMarks
```

Invalid:

```text
age
student
1Age
_Student
```

Example:

```text
num Age = 20\
sent Student_Name = "Sam"\
```

---

# 4. Data Types

Samet currently defines four basic data types.

| Samet Type | Meaning | Example |
|---|---|---|
| `num` | Integer number | `num Age = 20\` |
| `sent` | String | `sent Name = "Sam"\` |
| `logic` | Boolean | `logic Active = true\` |
| `letter` | Character | `letter Grade = 'A'\` |

## 4.1 `num`

`num` currently represents integer values.

```text
num Age = 20\
num Count = 100\
```

Floating-point literals are not currently supported.

Therefore:

```text
num Price = 19.99\
```

is invalid in the current language.

---

## 4.2 `sent`

`sent` represents strings.

Strings are enclosed in double quotes:

```text
sent Name = "Sameer"\
sent Message = "Hello World"\
```

---

## 4.3 `logic`

`logic` represents boolean values.

The two boolean literals are:

```text
true
false
```

Example:

```text
logic Active = true\
logic Finished = false\
```

Samet boolean keywords are lowercase.

Because Samet is case-sensitive:

```text
true
```

is a boolean literal, while:

```text
True
```

is treated as an identifier candidate and does not represent the boolean literal.

---

## 4.4 `letter`

`letter` represents a single character.

Characters use single quotes:

```text
letter Grade = 'A'\
letter Symbol = '#'\
```

A character literal must contain exactly one character.

For example, this is invalid:

```text
letter Grade = 'AB'\
```

---

# 5. Variable Declaration

Variables are declared by writing the type, identifier, assignment operator, expression, and statement terminator.

General form:

```text
type Identifier = expression\
```

Examples:

```text
num Age = 20\
sent Name = "Sam"\
logic Student = true\
letter Grade = 'A'\
```

The declaration creates a variable in the runtime environment.

Conceptually:

```text
num Age = 20\
```

creates:

```text
Age → 20
```

---

# 6. Assignment

An existing variable can be assigned a new value.

General form:

```text
Identifier = expression\
```

Example:

```text
num Age = 20\
Age = 25\
```

Assignment does not declare a new variable.

Assigning to an undeclared variable produces a runtime error.

Example:

```text
Age = 25\
```

when `Age` has not previously been declared is invalid at runtime.

---

# 7. Output

Samet uses `write<>` for output.

General form:

```text
write<expression>\
```

Examples:

```text
write<Age>\
write<"Hello">\
write<Age + 10>\
write<Age > 18>\
```

The expression inside `< >` is evaluated before being printed.

Note:

`<` and `>` are also comparison operators. The parser therefore distinguishes the closing `>` of `write<...>` from a greater-than comparison based on the surrounding expression structure.

---

# 8. Expressions

Expressions produce values.

Examples:

```text
20
Age
Age + 10
Age > 18
Age == 20
Age > 18 && Age < 60
```

Samet supports:

- Literals
- Identifiers
- Parenthesized expressions
- Unary expressions
- Binary expressions

---

# 9. Arithmetic Operators

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `^` | Exponentiation |

Examples:

```text
write<10 + 5>\
write<10 - 5>\
write<10 * 5>\
write<10 / 5>\
write<2 ^ 3>\
```

The Samet exponentiation operator is:

```text
^
```

The interpreter currently maps it to Python's exponentiation operation.

---

# 10. Comparison Operators

| Operator | Meaning |
|---|---|
| `<` | Less than |
| `<=` | Less than or equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |

Examples:

```text
write<Age < 18>\
write<Age <= 18>\
write<Age > 18>\
write<Age >= 18>\
```

Comparison expressions produce a boolean result.

---

# 11. Equality Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |

Examples:

```text
write<Age == 20>\
write<Age != 20>\
```

---

# 12. Logical Operators

Samet supports:

| Operator | Meaning |
|---|---|
| `&&` | Logical AND |
| `||` | Logical OR |
| `!` | Logical NOT |

Examples:

```text
write<Age > 18 && Age < 60>\
write<Age < 18 || Age > 60>\
write<!Active>\
```

`&&` and `||` are operators.

The keyword `or` is different: it is used for the alternative branch of an `if` statement.

---

# 13. Operator Precedence

From highest precedence to lowest:

```text
1. ^
2. * /
3. + -
4. < <= > >=
5. == !=
6. &&
7. ||
```

Unary operators are handled at the unary-expression level.

Parentheses can be used to explicitly control grouping.

Example:

```text
Age + 10 * 2
```

is interpreted as:

```text
Age + (10 * 2)
```

while:

```text
(Age + 10) * 2
```

forces the addition to happen first.

---

# 14. Unary Operators

Samet supports:

```text
!
-
```

Examples:

```text
write<!Active>\
write<-Age>\
```

Unary operators apply to the expression immediately following them.

---

# 15. Parentheses

Parentheses can be used to group expressions:

```text
write<(Age + 10) * 2>\
```

The expression inside parentheses is parsed as a single grouped expression.

---

# 16. Conditional Statements

Samet uses `if` for conditional execution.

Basic form:

```text
if [condition] {
    statements
}
```

Example:

```text
if [Age > 18] {
    write<"Adult">\
}
```

The condition is evaluated.

If it is `true`, the statements inside `{ }` are executed.

If it is `false`, they are skipped.

---

# 17. Alternative Branch

Samet uses the keyword `or` instead of `else`.

Example:

```text
if [Age > 18] {
    write<"Adult">\
}
or {
    write<"Minor">\
}
```

Semantics:

```text
condition == true
    ↓
execute first block

condition == false
    ↓
execute `or` block
```

The keyword:

```text
or
```

is therefore a control-flow keyword and is distinct from:

```text
||
```

which is the logical OR operator.

---

# 18. Blocks

Blocks are enclosed in:

```text
{
}
```

A block contains zero or more statements.

Example:

```text
{
    write<"Hello">\
    write<"World">\
}
```

Blocks are currently used by conditional statements.

---

# 19. Complete Example

A small Samet program can look like:

```text
num Age = 20\
sent Name = "Sameer"\
logic Student = true\
letter Grade = 'A'\

Age = Age + 1\

write<Name>\
write<Age>\
write<Grade>\

if [Age > 18 && Student == true] {
    write<"Adult student">\
}
or {
    write<"Not an adult student">\
}
```

The implementation processes this through:

```text
Source Code
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
AST
    ↓
Interpreter
    ↓
Environment + Execution
    ↓
Output
```

---

# 20. Runtime Environment

The interpreter maintains an environment containing variables.

Conceptually:

```text
Environment
┌────────────┬──────────────┐
│ Name       │ Value        │
├────────────┼──────────────┤
│ Age        │ 21           │
│ Name       │ "Sameer"     │
│ Student    │ true         │
│ Grade      │ 'A'          │
└────────────┴──────────────┘
```

Variable declarations create entries.

Assignments modify existing entries.

Identifier expressions retrieve values from the environment.

---

# 21. Interpreter Model

Samet is currently implemented as a tree-walking interpreter.

For example:

```text
Age + 10
```

is represented by an AST:

```text
        +
       / \
     Age  10
```

The interpreter recursively evaluates the left and right branches and then applies the operator.

For:

```text
Age + 10
```

if:

```text
Age → 20
```

the interpreter evaluates:

```text
Age → 20
10  → 10

20 + 10 → 30
```

---

# 22. Errors

Samet has errors at different stages of execution.

## Lexical errors

These occur when the lexer encounters invalid characters or invalid lexical forms.

Example:

```text
num Age = 20 @\
```

The `@` character is not currently a recognized Samet token.

---

## Syntax errors

These occur when the token sequence does not follow Samet's grammar.

Example:

```text
num Age 20\
```

The assignment operator `=` is missing.

---

## Runtime errors

These occur after a syntactically valid program begins executing.

Example:

```text
Age = 20\
```

when `Age` has never been declared.

The interpreter reports an undefined-variable runtime error.

---

# 23. Current Grammar

The current core grammar can be summarized as:

```text
program = statement*

statement =
      declaration_stmt
    | assignment_stmt
    | write_stmt
    | if_stmt

declaration_stmt =
    type IDENTIFIER '=' expression '\'

assignment_stmt =
    IDENTIFIER '=' expression '\'

write_stmt =
    'write' '<' expression '>' '\'

if_stmt =
    'if' '[' expression ']' '{' statement* '}'
    ('or' '{' statement* '}')?

type =
      'num'
    | 'sent'
    | 'logic'
    | 'letter'
```

Expression grammar:

```text
expression = logical_or

logical_or =
    logical_and ('||' logical_and)*

logical_and =
    equality ('&&' equality)*

equality =
    comparison (('==' | '!=') comparison)*

comparison =
    term (('<' | '<=' | '>' | '>=') term)*

term =
    factor (('+' | '-') factor)*

factor =
    power (('*' | '/') power)*

power =
    unary ('^' unary)*

unary =
      ('!' | '-') unary
    | primary

primary =
      NUMBER
    | STRING
    | CHAR
    | BOOLEAN
    | IDENTIFIER
    | '(' expression ')'
```

---

# 24. Samet vs Python and Java

Samet is **not currently a Python-to-Samet or Samet-to-Java translator**.

Python is the implementation language of the Samet interpreter.

However, the syntax can be compared with familiar languages:

| Concept | Samet | Python | Java |
|---|---|---|---|
| Integer | `num Age = 20\` | `Age = 20` | `int Age = 20;` |
| String | `sent Name = "Sam"\` | `Name = "Sam"` | `String Name = "Sam";` |
| Boolean | `logic Active = true\` | `Active = True` | `boolean Active = true;` |
| Character | `letter Grade = 'A'\` | `Grade = 'A'` | `char Grade = 'A';` |
| Output | `write<Age>\` | `print(Age)` | `System.out.println(Age);` |
| Addition | `A + B` | `A + B` | `A + B` |
| Power | `A ^ B` | `A ** B` | `Math.pow(A, B)` |
| AND | `A && B` | `A and B` | `A && B` |
| OR | `A || B` | `A or B` | `A || B` |
| NOT | `!A` | `not A` | `!A` |
| If | `if [A > B] { ... }` | `if A > B:` | `if (A > B) { ... }` |
| Else | `or { ... }` | `else:` | `else { ... }` |

These comparisons describe **syntax/semantic analogies**, not claims that Samet is implemented by translating into Python or Java.

---

# 25. Current Implementation Status

### Implemented

- [x] Lexer
- [x] Token definitions
- [x] Keywords
- [x] Identifiers
- [x] Integer literals
- [x] String literals
- [x] Character literals
- [x] Boolean literals
- [x] Arithmetic operators
- [x] Comparison operators
- [x] Equality operators
- [x] Logical operators
- [x] Parentheses
- [x] Comments
- [x] Variable declarations
- [x] Variable assignments
- [x] `write<>`
- [x] `if`
- [x] `or`
- [x] Blocks
- [x] AST generation
- [x] Runtime environment
- [x] Basic interpreter
- [x] Arithmetic evaluation
- [x] Comparison evaluation
- [x] Logical evaluation

### Planned

- [ ] Formal runtime type checking
- [ ] Improved runtime type representation
- [ ] Better boolean output formatting
- [ ] `while` loops
- [ ] Functions
- [ ] Function parameters
- [ ] `return`
- [ ] Local scopes
- [ ] User input
- [ ] More data structures
- [ ] String operations
- [ ] Standard library
- [ ] Improved error messages
- [ ] Automated language tests

The planned list may change as Samet evolves.

---

# 26. Project Architecture

```text
Samet/
│
├── main.py
├── syntax_tree.py
├── LANGUAGE_SPEC.md
│
├── lexer/
│   ├── __init__.py
│   ├── tokens.py
│   └── lexer.py
│
├── parser/
│   ├── __init__.py
│   └── parser.py
│
└── interpreter/
    ├── __init__.py
    └── interpreter.py
```

### `lexer/`

Converts source code into tokens.

### `parser/`

Converts tokens into an Abstract Syntax Tree.

### `syntax_tree.py`

Defines the AST node structures.

### `interpreter/`

Evaluates the AST and executes the program.

### `main.py`

Connects the stages together.

---

# 27. Development Philosophy

Samet is being developed incrementally.

The current priority is to make a small set of language features work completely from:

```text
source → lexer → parser → AST → interpreter → output
```

before expanding the language with additional constructs.

New language features should be documented in this specification when their syntax and behavior become stable.

---

## Version

**Samet Language Specification — 0.1 (Work in Progress)**

This specification describes the current development state of Samet and may change as the language evolves.
