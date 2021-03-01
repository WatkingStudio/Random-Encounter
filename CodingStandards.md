# General Style
* Use double-quoted strings
* Always surround binary operators with a single space on either side.
* Have one statement per line.
* For singletons use ‘is’ or ‘is not’ instead of equality operators
* Object type comparisons should always use ‘isinstance()’ instead of comparing types directly.
* Don’t compare boolean values to True or False using ‘==’
* Avoid trailing whitespace
* As long as you don’t sacrifice readability keep code explicit  

# Code Layout
## Indentation
* Use 4 spaces per indentation level
* Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces.
* When the conditional part of an if-statement is long enough to require that it can be written across multiple lines, the additional lines should include an extra indentation to differentiate it from other lines of code.
* The closing brace/bracket/parenthesis on multiline constructs should be lined up under the first character of the line that starts the multi-line construct.
## Blank Lines
* Method definitions should be surrounded by a single blank line.
* Extra blank lines may be used to separate groups of related functions.
* Use blank lines in functions, sparingly, to indicate logical sections.
## Imports
* Imports should be on separate lines
* Imports should always be put at the top of the file, after any module comments and docstrings, and before module globals and constants.
* They should be grouped in the following order:
* Standard Library Imports
* Related Third Part Imports
* Local Application/Library Specific Imports
# Comments
* Comments that contradict the code are worse than no comments. Always update comments when the code changes.
* Comments should be complete sentences.
* Ensure that your comments are clear and easily understandable to readers.
## Block Comments
Block comments generally apply to some code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space. Paragraphs inside a block comment should be separated by a line containing a single #.
## Inline Comments
Inline comments should be used sparingly, and should only be used if the line of code is not obvious. An inline comment should be separated by at least two spaces from the statement. They should start with a # and a single space. 
# Naming Conventions
* Local variables and parameter variables should use camelCase
* Global variables and member variables should use PascalCase
* Class names and Method names should use PascalCase
* Constants should be written in all capital letters
