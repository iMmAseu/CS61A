## Python Basics

### Expressions and statements

Programs are made up of expressions and statements. An *expression* is a piece of code that evaluates to some value and a *statement* is one or more lines of code that make something happen in a program.

When you enter a Python expression into the interactive Python interpreter, its value will be displayed. As you read through the following examples, try out some similar expressions on your own Python interpreter, which you can start up by typing this in your terminal:

```
python3
```

### Primitive expressions

Primitive expressions only take one step to evaluate. These include numbers and booleans, which just evaluate to themselves.

```
>>> 3
3
>>> 12.5
12.5
>>> True
True
```

### Arithmetic expressions

Numbers may be combined with mathematical operators to form compound expressions. In addition to the `+` operator (addition), the `-` operator (subtraction), the `*` operator (multiplication) and the `**` operator (exponentiation)(指数运算), there are three division-like operators to remember:

- Floating point division (`/`): divides the first number number by the second, evaluating to a number with a decimal point *even if the numbers divide evenly*.
- Floor division (`//`): divides the first number by the second and then rounds down, evaluating to an integer.(只保留整数部分)
- Modulo (`%`): evaluates to the positive remainder left over from division.

Parentheses may be used to group subexpressions together; the entire expression is evaluated in PEMDAS order.

```
>>> 7 / 4
1.75
>>> (2 + 6) / 4
2.0
>>> 7 // 4        # Floor division (rounding down)
1
>>> 7 % 4         # Modulus (remainder of 7 // 4)
3
```

### Assignment statements

An assignment statement consists of a name and an expression. It changes the state of the program by evaluating the expression to the right of the `=` sign and *binding* its value to the name on the left.

```
>>> a = (100 + 50) // 2
```

Now, if we evaluate `a`, the interpreter will display the value 75.

```
>>> a
75
```

### Understanding problems

Labs will also consist of function writing problems. Open up `lab00.py` in your text editor. You can type `open .` on MacOS or `start .` on Windows to open the current directory in your Finder/File Explorer. Then double click or right click to open the file in your text editor. You should see something like this:

```
def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return ______
```



The lines in the triple-quotes `"""` are called a **docstring**, which is a description of what the function is supposed to do. When writing code in 61A, you should always read the docstring!

The lines that begin with `>>>` are called **doctests**. Recall that when using the Python interpreter, you write Python expressions next to `>>>` and the output is printed below that line. Doctests explain what the function does by showing actual Python code. It answers the question: "If we input this Python code, what should the expected output be?"

In `twenty_twenty`,

- The docstring tells you to "come up with the most creative expression that evaluates to 2020," but that you can only use numbers and arithmetic operators `+` (add), `*` (multiply), and `-` (subtract).
- The doctest checks that the function call `twenty_twenty()` should return the number 2020.

## Appendix: Useful Python command line options

When running a Python file, you can use options on the command line to inspect your code further. Here are a few that will come in handy. If you want to learn more about other Python command-line options, take a look at the [documentation](https://docs.python.org/3.4/using/cmdline.html).

- Using no command-line options will run the code in the file you provide and return you to the command line.

  ```
  python3 
  ```

- **`-i`**: The `-i` option runs your Python script, then opens an interactive session. In an interactive session, you run Python code line by line and get immediate feedback instead of running an entire file all at once. To exit, type `exit()` into the interpreter prompt. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

  If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

  ```
  python3 -i 
  ```

- **`-m doctest`**: Runs doctests in a particular file. Doctests are surrounded by triple quotes (`"""`) within functions.

  Each test in the file consists of `>>>` followed by some Python code and the expected output (though the `>>>` are not seen in the output of the doctest command).

  ```
   python3 -m doctest 
  ```

## Testing with Ok

After writing some code, you can test your code with `ok` in various ways.

### Test specific questions

To test a specific question, use the `-q` option with the name of the question:

```
python3 ok -q <question>
```

### Test all questions

You can run all the tests with the following command:

```
python3 ok
```

### Display all tests

By default, only tests that **fail** will appear. If you want to see how you did on all tests, you can use the `-v` option:

```
python3 ok -v
```

### Test locally

If you do not want to send your progress to our server or you have any problems logging in, add the `--local` flag to block all communication:

```
python3 ok --local
```

### Adding your own tests

![image-20240208214224148](C:\Users\immasunnyboy\AppData\Roaming\Typora\typora-user-images\image-20240208214224148.png)

You can write your own tests and run them using `ok`. By default, a test file will be named `mytests.rst`. You may use a different name, but you will need to specify it when running tests.

### Running your own tests

To run all your tests in `mytests.rst` with verbose results:

```
python3 ok -t -v
```

If you put your tests in a different file or split your tests up into multiple files:

```
python3 ok -t your_new_filename.rst
```

To run just the tests from suite 1 case 1 in `mytests.rst`:

```
python3 ok -t --suite 1 --case 1
```

You might have noticed that there's a "test coverage" percentage for your tests (note that coverage statistics are only returned when running all tests). This is a measure of your test's [code coverage](https://en.wikipedia.org/wiki/Code_coverage).

To receive guidance on which lines you should test to increase your coverage:

```
python3 ok -t -cov
```

Code coverage won't include `ok` tests, so the coverage percentage might be higher in reality.

While code coverage is a useful tool, you should not get fixated on this number. It is better to write tests that help you complete the problem and make life easier instead of achieving a higher coverage.

### Submit assignment

When you are ready to submit, run `ok` with the `--submit` option:

```
python3 ok --submit
```

After submitting, `ok` will display a submission URL, with which you can view your submission on [okpy.org](https://okpy.org/).