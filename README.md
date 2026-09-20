# Samet

> A small programming language built from scratch in Python to understand how programming languages work internally.

**Status:** Work in Progress  
**Version:** 0.1  
**Implementation:** Python  
**Type:** Tree-walking interpreter

---

## About

Samet is an experimental programming language being built from scratch in Python.

The goal is to understand the complete journey from source code to execution while building the language incrementally:

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

The project is being developed as both a programming-language project and a learning project.

For the **complete syntax, grammar, operators, data types, examples, runtime behavior, errors, and language rules**, see:

**[LANGUAGE_SPEC.md](LANGUAGE_SPEC.md)**

---

## Current Status

Samet currently has the core pipeline working:

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
Execution
```

The implemented system currently includes:

- Custom lexer/tokenizer
- Token definitions
- Parser with operator precedence
- Abstract Syntax Tree (AST)
- Runtime environment
- Tree-walking interpreter
- Basic variable handling
- Expressions
- Conditional execution

For the exact list of implemented and planned language features, refer to the **[Language Specification](LANGUAGE_SPEC.md)**.

---

## Quick Example

A small Samet program:

```text
num Age = 20\
Age = Age + 1\

if [Age > 18] {
    write<"Adult">\
}
or {
    write<"Minor">\
}
```

This source code is processed through the Samet pipeline and executed by the interpreter.

For the complete syntax and semantics of this example, see **[LANGUAGE_SPEC.md](LANGUAGE_SPEC.md)**.

---

## Project Architecture

```text
                    Samet Source
                         │
                         ▼
                      Lexer
                         │
                         │ Tokens
                         ▼
                      Parser
                         │
                         │ AST
                         ▼
                    Interpreter
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Environment             Execution
              │                     │
              └──────────┬──────────┘
                         ▼
                       Output
```

### Main Components

| Component | Responsibility |
|---|---|
| `lexer/` | Converts source code into tokens |
| `parser/` | Converts tokens into an AST |
| `syntax_tree.py` | Defines AST node structures |
| `interpreter/` | Evaluates the AST and executes programs |
| `main.py` | Connects the stages together |
| `LANGUAGE_SPEC.md` | Defines Samet's language rules |

The implementation details are intentionally kept separate from the language specification.

---

## Project Structure

```text
Samet/
├── examples/
│
├── interpreter/
│   ├── __init__.py
│   └── interpreter.py
│
├── lexer/
│   ├── __init__.py
│   ├── lexer.py
│   └── tokens.py
│
├── parser/
│   ├── __init__.py
│   └── parser.py
│
├── syntax_tree.py
├── main.py
├── LANGUAGE_SPEC.md
└── README.md
```

---

## Running Samet

### Requirements

- Python 3.8+
- No external Python packages are currently required.

### Run

From the project directory:

```bash
python main.py
```

`main.py` is currently the entry point that connects the lexer, parser, and interpreter.

---

## Documentation

### Language Specification

**[Read the complete Samet Language Specification →](LANGUAGE_SPEC.md)**

The specification is the authoritative document for:

- syntax
- grammar
- data types
- operators
- precedence
- statements
- control flow
- runtime behavior
- errors
- Python/Java correlations
- implementation status

The README intentionally does **not** duplicate those rules. This keeps the project documentation easier to maintain: language behavior belongs in `LANGUAGE_SPEC.md`, while this README focuses on the project itself.

---

## Development Roadmap

The project is being developed incrementally.

Current development is focused on completing the runtime and making the existing language features work reliably from source code through execution.

Future development may include:

```text
while loops
functions
parameters and return values
local scopes
type checking
user input
arrays / collections
additional data types
standard library
improved diagnostics
automated language tests
possible compiler / transpiler work
```

These are development goals rather than current language features. The authoritative implementation status is maintained in **[LANGUAGE_SPEC.md](LANGUAGE_SPEC.md)**.

---

## Why Samet?

Building a programming language from scratch makes several concepts visible that are normally hidden behind high-level language tooling:

- lexical analysis
- tokenization
- grammar design
- parsing
- operator precedence
- AST construction
- expression evaluation
- runtime environments
- runtime errors
- type systems
- control flow
- scopes
- interpreters and compilers

Samet is being built one component at a time to understand these concepts by implementing them rather than only studying them theoretically.

---

## Repository Documentation

| Document | Purpose |
|---|---|
| [`README.md`](README.md) | Project overview and architecture |
| [`LANGUAGE_SPEC.md`](LANGUAGE_SPEC.md) | Authoritative Samet language specification |

---

> Samet is a work in progress. The implementation and language specification may evolve as new features are designed and tested.
