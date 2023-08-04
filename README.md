
# Python
Learning Space for Python

# Virtual Environment
When moving a program from one machine to another with different Python versions or library versions, issues can arise.

Installing the latest version of libraries without consideration can disrupt other programs on the target machine.

Python's solution is to use a virtual environment, which is a self-contained copy of everything required to run the program.

The virtual environment ensures access to the correct Python version and necessary libraries.

The basic workflow involves creating a separate virtual environment, specifying the required Python version and libraries, and developing the program within this isolated environment.

  ## Create a Virtual Environment
  - You create a virtual environment by calling the venv  module. 

      ```python
        python -m venv env
      ```

 - The directories look like this in Windows:
  /env
    /include
    /lib
    /Scripts

The directories look like this in Linux and macOS:
  /env
    /bin
    /include
    /lib


Avoid placing your program files within the "env" directory. Instead, it's recommended to organize your code files in a directory named "src" or a similar alternative.

### Activate Virtual Environment
  ```python
    C:\ .. \env\Scripts\activate
  ```
![Activate Virtual Environment](https://github.com/saurabh7ar/python/assets/132929888/450f710c-72be-492c-b791-4712e5c7ff89)
