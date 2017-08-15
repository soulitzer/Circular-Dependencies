# CircularDependencies
Finds circular dependencies in Javascript projects

Looks for 'require' statements recursively to create a digraph of all the dependencies between the files in a project. Recursively remove edges until the graph no longer contains cycles. Returns an array of all the cycles that were detected.

1. Point the DIRECTORY variable in the bash file to the desired directory
2. Run the bash file to generate 'output.txt' which stores info about the dependency structure
3. Run the python file in the same directory as output.txt

Optional: Create an ignored.txt file to ignore certain files while searching for cycles.

Developed while working at [Omninox](https://omninox.org/)




