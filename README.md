# ontario-gpa-calculator

Tool built for personal use to calculate gpa easily

# Usage
- git clone
- create a file to put your new line separated grades in, add one comma to enter the course weight to the right
  - default course weight is 0.5
  - example file will be shown below
- ``python3 calc.py filename.txt``

Example file contents with your grades for a student who took 3 0.5 courses and one 0.75 course
```
75
80
89,0.75
83
```

# TODO
- re-write this in TypeScript / JS
- Convert this into a static web page anyone can access in a browser
- More usable user input
- Ability to paste an unofficial University of Guelph transcript and output GPA 
- Include other province's GPA calculations (https://gpacalculator.net/grade-conversion/canada/)
