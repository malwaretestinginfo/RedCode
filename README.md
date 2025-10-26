# RedCode Programming Language

RedCode is a Python-based programming language where all commands start with "red" and require semicolons after each statement.

## Installation & Usage

```bash
python redcode.py demo.red
```

## Syntax

- All files must have `.red` extension
- Every statement must end with a semicolon `;`
- All functions start with `red`
- Comments start with `#`

## 🚀 External Modules with Auto-Wrapping

RedCode can import Python modules and automatically creates "red"-prefixed wrappers:

```redcode
# HTTP Requests
redexternal requests;
response = redget("https://httpbin.org/json");
redprint("Status:", response["status_code"]);
redprint("Data:", response["text"]);

# JSON processing
redexternal json;
data = redloads('{"name": "RedCode", "version": 1.0}');
redprint("Name:", data["name"]);
json_string = reddumps(data);

# Time functions
redexternal time;
redprint("Waiting 2 seconds...");
redsleep(2);
redprint("Current time:", redtime());

# Random numbers
redexternal random;
number = redrandint(1, 100);
choices = redlist("apple", "banana", "cherry");
choice = redchoice(choices);
redprint("Random choice:", choice);
```

### Supported Modules with Auto-Wrapping:
- **requests**: `redget()`, `redpost()`, `redput()`, `reddelete()`, `redpatch()`
- **json**: `redloads()`, `reddumps()`, `redload()`, `reddump()`
- **time**: `redsleep()`, `redtime()`, `redstrftime()`, `redstrptime()`
- **random**: `redrandint()`, `redchoice()`, `redshuffle()`, `redrandom()`
- **datetime**: `rednow()`, `redtoday()`, `redstrftime()`
- **base64**: `redb64encode()`, `redb64decode()`
- **hashlib**: `redmd5()`, `redsha1()`, `redsha256()`

## Core Functions

### Input/Output
- `redprint(...)` - Print to console
- `redinput(prompt)` - Get user input

### Data Types & Conversion
- `redtype(obj)` - Get object type
- `redint(value)` - Convert to integer
- `redstr(value)` - Convert to string
- `redfloat(value)` - Convert to float
- `redlen(obj)` - Get object length

### Math Functions
- `redabs(x)` - Absolute value
- `redmax(...)` - Maximum value
- `redmin(...)` - Minimum value
- `redsum(iterable)` - Sum of values
- `redround(number, digits)` - Round number
- `redpow(base, exp)` - Power function
- `redsqrt(x)` - Square root

### String Functions
- `redupper(s)` - Convert to uppercase
- `redlower(s)` - Convert to lowercase
- `redstrip(s)` - Remove whitespace
- `redsplit(s, delimiter)` - Split string
- `redjoin(delimiter, iterable)` - Join strings
- `redreplace(s, old, new)` - Replace substring

### List Functions
- `redlist(...)` - Create list
- `redappendlist(lst, item)` - Append item
- `redpop(lst, index)` - Remove item
- `redsort(lst, reverse)` - Sort list
- `redsorted(lst, reverse)` - Get sorted copy

### File Operations
- `redread(filename)` - Read file
- `redwrite(filename, content)` - Write file
- `redappend(filename, content)` - Append to file
- `redexists(path)` - Check if exists
- `redlistdir(path)` - List directory

## Examples

### Basic Example
```redcode
# Define variables
name = "RedCode";
version = 1.0;

# Output
redprint("Welcome to", name, version);

# Create list
numbers = redlist(5, 2, 8, 1, 9);
sorted_nums = redsorted(numbers);
redprint("Sorted:", sorted_nums);
```

### HTTP API Example
```redcode
# API Request
redexternal requests;
redexternal json;

response = redget("https://jsonplaceholder.typicode.com/posts/1");
redprint("Status:", response["status_code"]);

if response["status_code"] == 200:
    data = redloads(response["text"]);
    redprint("Title:", data["title"]);
```

## Syntax Highlighting

For better syntax highlighting in Kiro:
1. Open a `.red` file
2. Click "Plain Text" in the bottom right
3. Select "Python" for similar highlighting

Or use the build script:
```bash
python build-syntax.py
```

## Demo File

Run the demo:
```bash
python redcode.py demo.red
```

The `demo.red` file showcases all RedCode features including external modules with automatic red-wrappers.
