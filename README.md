# BrainFart
Esoteric programming language made in Python. Inspired by the esoteric language: "BrainF***".

In this repo I have made an example .bfart file, that outputs "Hello World" when executed using main.py. I've also included some other examples to show how loops work

# Syntax
The syntax of this programming language is very easy. Newlines and spaces do not matter. You can write a comment using $ at the start of the line. Inline comments don't work.

# Commands
### Cell manipulation

!: Create a new cell

?: Remove last cell

x: Initialize all cells, and set them to 0

:: Increase cell value limit

;: Increase cell limit


### Move pointer

r: Move the pointer right

l: Move the pointer left

### Change cell values

a: Add 1 to current cell

A: Add 10 to current cell

s: Subtract 1 from current cell

S: Subtract 10 from current cell

m: Multiplies current cell by 10

d: Divides current cell by 10

{: Mutliplies value on the left by value in current cell

}: Multiplies value on the right by value in current cell

\>: Copies value in current cell to the cell on the right

<: Copies value in current cell to the cell on the left

c: Clears current cell

C: Clears all cells


### Logic

=: Checks if current cell and the one behind are equal, if they are equal move pointer 1 spot to the right, else do nothing


### Loops

[: Start of a loop

]: Jumps back to previous [ if current cell is not 0


### Outputting/Inputting

o: Adds current cell to output

O: Adds all cells to output

i: Get first character from input and puts value in current cell

I: Get string input, fills all cells

*: Get integer value from input

p: Forces print output

P: Clears output

@: Prints integer value at current cell

#: Debug command, prints all cells and the pointers location

### File Reading
/: Loads code from another .bfart file. (Requires its own line!)
