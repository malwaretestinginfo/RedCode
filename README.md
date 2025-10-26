# RedCode Programming Language

RedCode is a comprehensive Python-based programming language interpreter that provides a rich, educational programming environment with extensive built-in functions and an enhanced external module system with automatic red-wrapper generation.

## 🚀 Key Features

- **Simple Syntax**: Easy-to-learn programming language with semicolon-terminated statements
- **Enhanced Module System**: Import external Python modules with automatic red-wrapper generation
- **50+ Built-in Functions**: Comprehensive function library covering all major programming needs
- **IDE Integration**: Native support for Kiro IDE and VS Code with syntax highlighting
- **Educational Focus**: Designed for learning programming concepts
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Automated Setup**: Build scripts for easy IDE integration

## 📦 Installation & Quick Start

### Prerequisites
- **Python 3.x** (no additional dependencies required)

### Running RedCode Programs

```bash
python redcode.py your_program.red
```

### Basic Example

Create `hello.red`:
```redcode
# Simple RedCode program
name = redinput("Enter your name: ");
redprint("Hello", name, "!");
redprint("Welcome to RedCode programming!");
```

Run it:
```bash
python redcode.py hello.red
```

## 🔧 Enhanced External Module System

RedCode features an advanced external module system that automatically generates red-prefixed wrapper functions for popular Python modules, making external libraries easier to use within RedCode programs.

### How It Works

When you import a module using `redexternal`, the interpreter:
1. **Imports the Python module** normally
2. **Auto-generates red-prefixed wrappers** for common functions
3. **Provides simplified APIs** with error handling
4. **Makes both original and wrapped functions available**

### Supported Modules with Auto-Wrappers

| Module | Auto-Generated Functions | Description |
|--------|-------------------------|-------------|
| **requests** | `redget`, `redpost`, `redput`, `reddelete`, `redpatch`, `redhead`, `redoptions` | HTTP client with simplified response handling |
| **json** | `redloads`, `reddumps`, `redload`, `reddump` | JSON parsing with error handling |
| **time** | `redtime`, `redsleep`, `redstrftime`, `redstrptime` | Time operations and formatting |
| **datetime** | `rednow`, `redtoday`, `redstrftime`, `redstrptime` | Date and time handling |
| **random** | `redrandint`, `redchoice`, `redshuffle`, `redrandom` | Random number and choice generation |
| **urllib** | `redurlopen`, `redurlretrieve` | URL handling operations |
| **base64** | `redb64encode`, `redb64decode` | Base64 encoding/decoding |
| **hashlib** | `redmd5`, `redsha1`, `redsha256` | Cryptographic hashing |

### Usage Examples

#### HTTP Requests (requests module)
```redcode
redexternal requests;

# Simple GET request with automatic response handling
response = redget("https://api.github.com/users/octocat");
redprint("Status Code:", response["status_code"]);
redprint("Response Text:", response["text"]);

# POST request with data
post_data = reddict(name="RedCode", version="1.0");
response = redpost("https://httpbin.org/post", json=post_data);
redprint("POST Response:", response["status_code"]);
```

#### JSON Operations (json module)
```redcode
redexternal json;

# Parse JSON string
json_text = '{"name": "RedCode", "version": 1.0}';
data = redloads(json_text);
redprint("Parsed data:", data);

# Convert to JSON string
my_data = reddict(language="RedCode", features=redlist("simple", "powerful"));
json_output = reddumps(my_data);
redprint("JSON output:", json_output);
```

#### Time Operations (time module)
```redcode
redexternal time;

# Get current timestamp
current = redtime();
redprint("Current time:", current);

# Sleep for 2 seconds
redprint("Sleeping...");
redsleep(2);
redprint("Done sleeping!");
```

#### Random Operations (random module)
```redcode
redexternal random;

# Generate random integer
num = redrandint(1, 100);
redprint("Random number:", num);

# Choose from list
options = redlist("apple", "banana", "cherry", "date");
choice = redchoice(options);
redprint("Random choice:", choice);
```

### Error Handling

Auto-generated wrappers include built-in error handling:

```redcode
redexternal requests;

# If request fails, returns error information
response = redget("https://invalid-url.com");
if "error" in response:
    redprint("Request failed:", response["error"]);
else:
    redprint("Success:", response["status_code"]);
```

## 📚 Built-in Functions (50+ Functions)

### Core Functions
| Function | Description | Example |
|----------|-------------|---------|
| `redprint()` | Print values to console | `redprint("Hello", name);` |
| `redinput()` | Get user input | `name = redinput("Enter name: ");` |
| `redlen()` | Get length of string/object | `length = redlen("Hello");` |
| `redtype()` | Get type of variable | `type = redtype(42);` |
| `redint()` | Convert to integer | `num = redint("123");` |
| `redstr()` | Convert to string | `text = redstr(42);` |
| `redfloat()` | Convert to float | `decimal = redfloat("3.14");` |
| `redexternal()` | Import Python modules with auto-wrappers | `redexternal("requests");` |

### Mathematical Functions
| Function | Description | Example |
|----------|-------------|---------|
| `redabs()` | Absolute value | `redabs(-5);` |
| `redmax()` | Maximum value | `redmax(1, 5, 3);` |
| `redmin()` | Minimum value | `redmin(1, 5, 3);` |
| `redsum()` | Sum of iterable | `redsum([1, 2, 3]);` |
| `redround()` | Round number | `redround(3.14159, 2);` |
| `redpow()` | Power function | `redpow(2, 3);` |
| `redsqrt()` | Square root | `redsqrt(16);` |

### String Functions
| Function | Description | Example |
|----------|-------------|---------|
| `redupper()` | Convert to uppercase | `redupper("hello");` |
| `redlower()` | Convert to lowercase | `redlower("HELLO");` |
| `redstrip()` | Remove whitespace | `redstrip("  text  ");` |
| `redsplit()` | Split string | `redsplit("a,b,c", ",");` |
| `redjoin()` | Join strings | `redjoin("-", ["a", "b"]);` |
| `redreplace()` | Replace substring | `redreplace("hello", "l", "x");` |
| `redstartswith()` | Check prefix | `redstartswith("hello", "he");` |
| `redendswith()` | Check suffix | `redendswith("hello", "lo");` |
| `redfind()` | Find substring | `redfind("hello", "ll");` |

### List Functions
| Function | Description | Example |
|----------|-------------|---------|
| `redlist()` | Create list | `redlist(1, 2, 3);` |
| `redappendlist()` | Append to list | `redappendlist(list, item);` |
| `redpop()` | Remove and return item | `redpop(list, index);` |
| `redinsert()` | Insert at index | `redinsert(list, 1, item);` |
| `redremoveitem()` | Remove item | `redremoveitem(list, item);` |
| `redindex()` | Find item index | `redindex(list, item);` |
| `redcount()` | Count occurrences | `redcount(list, item);` |
| `redsort()` | Sort list in-place | `redsort(list, reverse=True);` |
| `redreverse()` | Reverse list in-place | `redreverse(list);` |

### Dictionary Functions
| Function | Description | Example |
|----------|-------------|---------|
| `reddict()` | Create dictionary | `reddict();` |
| `redkeys()` | Get dictionary keys | `redkeys(dict);` |
| `redvalues()` | Get dictionary values | `redvalues(dict);` |
| `reditems()` | Get dictionary items | `reditems(dict);` |
| `redget()` | Get with default | `redget(dict, key, default);` |

### File and OS Functions
| Function | Description | Example |
|----------|-------------|---------|
| `redopen()` | Open file | `redopen("file.txt", "r");` |
| `redread()` | Read entire file | `redread("file.txt");` |
| `redwrite()` | Write to file | `redwrite("file.txt", content);` |
| `redappend()` | Append to file | `redappend("file.txt", content);` |
| `redexists()` | Check if path exists | `redexists("file.txt");` |
| `redlistdir()` | List directory | `redlistdir(".");` |
| `redmkdir()` | Create directory | `redmkdir("newdir");` |
| `redremove()` | Remove file | `redremove("file.txt");` |
| `redcwd()` | Get current directory | `redcwd();` |
| `redchdir()` | Change directory | `redchdir("path");` |

### Utility Functions
| Function | Description | Example |
|----------|-------------|---------|
| `redrange()` | Create range | `redrange(5);` or `redrange(2, 8);` |
| `redenumerate()` | Enumerate iterable | `redenumerate(list);` |
| `redzip()` | Zip iterables | `redzip(list1, list2);` |
| `redfilter()` | Filter iterable | `redfilter(func, list);` |
| `redmap()` | Map function | `redmap(func, list);` |
| `redany()` | Check if any true | `redany([True, False]);` |
| `redall()` | Check if all true | `redall([True, True]);` |
| `redsorted()` | Return sorted copy | `redsorted(list, reverse=True);` |
| `redreversed()` | Return reversed copy | `redreversed(list);` |

## 🎨 IDE Support

### Kiro IDE (Native Support)
RedCode has native Kiro IDE support with built-in language configuration:

#### Features:
- 🎨 **Native Language Definition**: Built-in RedCode language support
- 📝 **File Association**: Automatic `.red` file recognition  
- 💬 **Comment Support**: Line comments with `#` token
- 📋 **Bracket Matching**: Support for `()`, `[]`, `{}` brackets
- 🔗 **Auto-Closing**: Automatic closing of brackets and quotes
- 🎯 **Workspace Integration**: Project-level language configuration
- 🌈 **Custom Color Scheme**: Optimized syntax highlighting colors

#### Setup:
RedCode files work immediately in Kiro IDE. For manual setup:
```bash
# Windows
cd syntax && install-kiro.bat

# Or use the automated builder
python build-syntax.py
```

#### Configuration Files:
- `.kiro/workspace.json` - Project workspace configuration
- `.kiro/settings/syntax.json` - Language syntax rules
- `syntax/language-support-kiro.json` - Complete language definition

### VS Code Support
Complete VS Code integration with custom syntax highlighting:

#### Installation Options:

**Option 1: Automated Installation (Recommended)**
```bash
python build-syntax.py
```

**Option 2: Manual Installation**
```bash
# Windows
cd syntax && install.bat

# Unix/Linux/macOS
cd syntax && chmod +x install.sh && ./install.sh
```

**Option 3: Interactive Installation**
```bash
# Windows - Choose your editor
cd syntax && install.bat
# Options: VS Code, Kiro IDE, or Both
```

#### Features:
- 🟡 **RedCode Functions** - Gold highlighting (`#DCDCAA`)
- 🔴 **Import Statements** - Red highlighting (`#FF6B6B`)
- 🟣 **Control Keywords** - Purple highlighting (`#C586C0`)
- 🟠 **Strings** - Orange highlighting (`#CE9178`)
- 🟢 **Comments** - Green highlighting (`#6A9955`)
- 🔵 **Numbers** - Light green highlighting (`#B5CEA8`)
- 🔵 **Variables** - Light blue highlighting (`#9CDCFE`)
- ⚪ **Semicolons** - White bold highlighting (`#D4D4D4`)
- 📝 **Code Snippets** - 10+ auto-completion snippets

#### Available Snippets:
| Prefix | Snippet | Description |
|--------|---------|-------------|
| `rp` | `redprint("text");` | Print statement |
| `rv` | `variable = value;` | Variable assignment |
| `re` | `redexternal module;` | External import |
| `rl` | `list = redlist(items);` | List creation |
| `rfr` | `content = redread("file");` | File read |
| `rfw` | `redwrite("file", "content");` | File write |
| `rfunc` | Function call template | Function with result |
| `rc` | Comment block | Multi-line comment |
| `rmath` | Math operations | Mathematical functions |
| `rstr` | String operations | String manipulation |

## 📋 Language Syntax

### Basic Syntax Rules
- All files must have `.red` extension
- Every statement must end with semicolon `;`
- All functions begin with `red`
- Comments start with `#`

### Variable Assignment
```redcode
variable_name = value;
```

### Function Calls
```redcode
redprint("Hello World");
result = redlen("test");
```

### Mathematical Expressions
```redcode
result = (a + b) * 2 - 5;
```

### Module Imports with Auto-Wrappers
```redcode
redexternal requests;  # Auto-generates: redget, redpost, redput, etc.
redexternal json;      # Auto-generates: redloads, reddumps, etc.
redexternal time;      # Auto-generates: redtime, redsleep, etc.
redexternal random;    # Auto-generates: redrandint, redchoice, etc.
```

### Control Structures
```redcode
# Conditional statements
if condition:
    redprint("True case");
elif other_condition:
    redprint("Elif case");
else:
    redprint("Else case");

# Loops
for item in redrange(5):
    redprint("Item:", item);

while condition:
    redprint("Loop iteration");
```

## 🧪 Demo & Testing

The project includes a comprehensive demo file:

### Demo File
| File | Purpose | Features Demonstrated |
|------|---------|----------------------|
| `demo.red` | Complete feature showcase | External modules, JSON/time/random operations, string/list manipulation |

### Running the Demo
```bash
# Run the comprehensive demo
python redcode.py demo.red
```

The demo showcases:
- External module imports with auto-wrappers
- JSON parsing and generation
- Time operations and delays
- Random number generation
- String and list manipulations
- Base64 encoding/decoding

## 🏗️ Project Structure

```
redcode/
├── redcode.py                          # Main interpreter (500+ lines)
├── demo.red                           # Comprehensive demo program
├── build-syntax.py                    # Automated syntax builder
├── README.md                          # This documentation
├── .kiro/                             # Kiro IDE configuration
│   ├── settings/
│   │   ├── syntax.json                # Kiro syntax configuration
│   │   └── language-support.json     # Language support config
│   └── workspace.json                 # Workspace configuration
├── .vscode/                           # VS Code configuration
│   ├── settings.json                  # VS Code syntax highlighting
│   └── extensions.json               # Extension recommendations
└── syntax/                            # Syntax highlighting package
    ├── package.json                   # VS Code extension manifest
    ├── redcode.tmLanguage.json        # TextMate grammar
    ├── language-configuration.json    # Language configuration
    ├── redcode-snippets.json         # Code snippets
    ├── language-support-kiro.json    # Kiro language support
    ├── vscode-settings.json          # VS Code specific settings
    ├── install-kiro.bat              # Kiro installation script
    ├── install.bat                    # Windows installer
    ├── install.sh                     # Unix installer
    └── README.md                      # Syntax package documentation
```

## 🔧 Architecture

### Core Components

1. **RedCodeInterpreter Class**: Main interpreter engine
   - Variable storage system (`self.variables`)
   - Enhanced module import tracking (`self.imported_modules`)
   - Automatic red-wrapper generation (`_generate_red_wrappers`)
   - Built-in function registry (50+ functions)
   - Expression evaluation engine
   - Safe execution environment

2. **Wrapper Generation System**:
   - Module-specific wrapper creators for popular libraries
   - Error handling integration
   - Simplified API generation
   - Both wrapped and original function access

3. **Parsing System**: 
   - Line-by-line parsing with semicolon validation
   - Comment and empty line handling
   - Syntax error detection with line numbers

4. **Execution Engine**:
   - Variable assignment handling
   - Expression evaluation with Python's `exec()`
   - Safe execution environment with restricted built-ins

### Security Features
- Restricted `__builtins__` to prevent dangerous operations
- Safe execution environment with limited scope
- Input validation and comprehensive error handling

## 🚀 Recent Updates

**Enhanced External Module System**:
- **Automatic Red-Wrapper Generation**: Popular modules get red-prefixed functions automatically
- **Simplified APIs**: External libraries wrapped with error handling and simplified interfaces
- **Module-Specific Handling**: Custom wrappers for requests, json, time, random, and more
- **Error Resilience**: Built-in error handling for external module operations

**Complete IDE Integration**:
- **Native Kiro Support**: Built-in language definition in `.kiro/workspace.json`
- **VS Code Extension**: Complete TextMate grammar and custom color scheme
- **Automated Installation**: Build scripts for easy setup across IDEs
- **Interactive Installers**: Choose your preferred IDE during setup

**Comprehensive Function Library**:
- 50+ built-in functions covering all major programming needs
- Advanced mathematical, string, list, and utility operations
- File I/O and directory management capabilities

## 🛠️ Development Tools

### Automated Build System
The `build-syntax.py` script provides automated setup for both IDEs:

```bash
python build-syntax.py
```

Features:
- **File Validation**: Checks all syntax files for validity
- **VS Code Extension**: Automatically installs to user extensions directory
- **Kiro Integration**: Configures native language support
- **Error Reporting**: Detailed feedback on installation status

### Manual Installation Scripts
- `syntax/install.bat` - Interactive Windows installer
- `syntax/install.sh` - Unix/Linux installer  
- `syntax/install-kiro.bat` - Kiro-specific installer

## 🤝 Contributing

This is an educational programming language project designed for learning and experimentation. The interpreter features:

- Clean, modular architecture for easy extension
- Comprehensive error handling with line-specific reporting
- Safe execution environment
- Foundation for additional language features

## 📄 License

This project is open source and available for educational purposes.

---

**RedCode** - Making Python programming more accessible with red-prefixed functions and automatic module wrapping! 🔴✨# RedCode Programming Language

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