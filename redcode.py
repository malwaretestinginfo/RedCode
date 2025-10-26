#!/usr/bin/env python3
"""
RedCode Interpreter - A Python-based programming language
Usage: python redcode.py <filename.red>
"""

import sys
import re
import os

class RedCodeInterpreter:
    def __init__(self):
        self.variables = {}
        self.imported_modules = {}
    
    def redprint(self, *args):
        """RedCode print function"""
        output = ' '.join(str(arg) for arg in args)
        print(output)
        return output
    
    def redinput(self, prompt=""):
        """RedCode input function"""
        return input(prompt)
    
    def redlen(self, obj):
        """RedCode length function"""
        return len(obj)
    
    def redtype(self, obj):
        """RedCode type function"""
        return type(obj).__name__
    
    def redint(self, value):
        """RedCode int conversion"""
        return int(value)
    
    def redstr(self, value):
        """RedCode string conversion"""
        return str(value)
    
    def redfloat(self, value):
        """RedCode float conversion"""
        return float(value)
    
    def redexternal(self, module_name):
        """RedCode import function with automatic red-wrapper generation"""
        try:
            if module_name not in self.imported_modules:
                # Import the actual module
                module = __import__(module_name)
                self.imported_modules[module_name] = module
                
                # Auto-generate red-wrapped functions for common modules
                self._generate_red_wrappers(module_name, module)
                
            return self.imported_modules[module_name]
        except ImportError as e:
            raise ImportError(f"Cannot import module '{module_name}': {e}")
    
    def _generate_red_wrappers(self, module_name, module):
        """Generate red-prefixed wrappers for module functions"""
        
        # Define common functions for popular modules
        module_functions = {
            'requests': ['get', 'post', 'put', 'delete', 'patch', 'head', 'options'],
            'json': ['loads', 'dumps', 'load', 'dump'],
            'time': ['sleep', 'time', 'strftime', 'strptime'],
            'datetime': ['now', 'today', 'strftime', 'strptime'],
            'random': ['randint', 'choice', 'shuffle', 'random'],
            'urllib': ['urlopen', 'urlretrieve'],
            'base64': ['b64encode', 'b64decode'],
            'hashlib': ['md5', 'sha1', 'sha256']
        }
        
        if module_name in module_functions:
            for func_name in module_functions[module_name]:
                red_func_name = f"red{func_name}"
                
                # Create wrapper function
                if hasattr(module, func_name):
                    original_func = getattr(module, func_name)
                    
                    # Special handling for different modules
                    if module_name == 'requests':
                        wrapper_func = self._create_requests_wrapper(original_func, func_name)
                    elif module_name == 'json':
                        wrapper_func = self._create_json_wrapper(original_func, func_name)
                    elif module_name == 'time':
                        wrapper_func = self._create_time_wrapper(original_func, func_name)
                    elif module_name == 'random':
                        wrapper_func = self._create_random_wrapper(original_func, func_name)
                    else:
                        wrapper_func = self._create_generic_wrapper(original_func, func_name)
                    
                    # Add to available functions
                    setattr(self, red_func_name, wrapper_func)
                    # Also add to variables for immediate access
                    self.variables[red_func_name] = wrapper_func
                    
        # Also make the original module available with red prefix
        red_module_name = f"red{module_name}"
        setattr(self, red_module_name, module)
    
    def _create_requests_wrapper(self, original_func, func_name):
        """Create wrapper for requests functions"""
        def wrapper(*args, **kwargs):
            try:
                response = original_func(*args, **kwargs)
                # Return a simplified response object
                return {
                    'status_code': response.status_code,
                    'text': response.text,
                    'json': lambda: response.json() if response.headers.get('content-type', '').startswith('application/json') else None,
                    'headers': dict(response.headers),
                    'url': response.url
                }
            except Exception as e:
                return {'error': str(e), 'status_code': 0}
        return wrapper
    
    def _create_json_wrapper(self, original_func, func_name):
        """Create wrapper for json functions"""
        def wrapper(*args, **kwargs):
            try:
                return original_func(*args, **kwargs)
            except Exception as e:
                return {'error': f"JSON {func_name} failed: {str(e)}"}
        return wrapper
    
    def _create_time_wrapper(self, original_func, func_name):
        """Create wrapper for time functions"""
        def wrapper(*args, **kwargs):
            return original_func(*args, **kwargs)
        return wrapper
    
    def _create_random_wrapper(self, original_func, func_name):
        """Create wrapper for random functions"""
        def wrapper(*args, **kwargs):
            return original_func(*args, **kwargs)
        return wrapper
    
    def _create_generic_wrapper(self, original_func, func_name):
        """Create generic wrapper for any function"""
        def wrapper(*args, **kwargs):
            try:
                return original_func(*args, **kwargs)
            except Exception as e:
                return {'error': f"{func_name} failed: {str(e)}"}
        return wrapper
    
    # File and OS operations
    def redopen(self, filename, mode='r'):
        """RedCode file open function"""
        return open(filename, mode)
    
    def redread(self, filename):
        """RedCode read entire file"""
        with open(filename, 'r') as f:
            return f.read()
    
    def redwrite(self, filename, content):
        """RedCode write to file"""
        with open(filename, 'w') as f:
            f.write(content)
        return True
    
    def redappend(self, filename, content):
        """RedCode append to file"""
        with open(filename, 'a') as f:
            f.write(content)
        return True
    
    def redexists(self, path):
        """RedCode check if file/directory exists"""
        return os.path.exists(path)
    
    def redlistdir(self, path='.'):
        """RedCode list directory contents"""
        return os.listdir(path)
    
    def redmkdir(self, path):
        """RedCode create directory"""
        os.makedirs(path, exist_ok=True)
        return True
    
    def redremove(self, path):
        """RedCode remove file"""
        os.remove(path)
        return True
    
    def redcwd(self):
        """RedCode get current working directory"""
        return os.getcwd()
    
    def redchdir(self, path):
        """RedCode change directory"""
        os.chdir(path)
        return True
    
    # Math operations
    def redabs(self, x):
        """RedCode absolute value"""
        return abs(x)
    
    def redmax(self, *args):
        """RedCode maximum value"""
        return max(args)
    
    def redmin(self, *args):
        """RedCode minimum value"""
        return min(args)
    
    def redsum(self, iterable):
        """RedCode sum of iterable"""
        return sum(iterable)
    
    def redround(self, number, digits=0):
        """RedCode round number"""
        return round(number, digits)
    
    def redpow(self, base, exp):
        """RedCode power function"""
        return pow(base, exp)
    
    def redsqrt(self, x):
        """RedCode square root"""
        import math
        return math.sqrt(x)
    
    # List operations
    def redlist(self, *args):
        """RedCode create list"""
        return list(args)
    
    def redappendlist(self, lst, item):
        """RedCode append to list"""
        lst.append(item)
        return lst
    
    def redpop(self, lst, index=-1):
        """RedCode pop from list"""
        return lst.pop(index)
    
    def redinsert(self, lst, index, item):
        """RedCode insert into list"""
        lst.insert(index, item)
        return lst
    
    def redremoveitem(self, lst, item):
        """RedCode remove item from list"""
        lst.remove(item)
        return lst
    
    def redindex(self, lst, item):
        """RedCode find index of item"""
        return lst.index(item)
    
    def redcount(self, lst, item):
        """RedCode count occurrences"""
        return lst.count(item)
    
    def redsort(self, lst, reverse=False):
        """RedCode sort list"""
        lst.sort(reverse=reverse)
        return lst
    
    def redreverse(self, lst):
        """RedCode reverse list"""
        lst.reverse()
        return lst
    
    # String operations
    def redupper(self, s):
        """RedCode uppercase string"""
        return s.upper()
    
    def redlower(self, s):
        """RedCode lowercase string"""
        return s.lower()
    
    def redstrip(self, s):
        """RedCode strip whitespace"""
        return s.strip()
    
    def redsplit(self, s, delimiter=' '):
        """RedCode split string"""
        return s.split(delimiter)
    
    def redjoin(self, delimiter, iterable):
        """RedCode join strings"""
        return delimiter.join(iterable)
    
    def redreplace(self, s, old, new):
        """RedCode replace in string"""
        return s.replace(old, new)
    
    def redstartswith(self, s, prefix):
        """RedCode check if string starts with prefix"""
        return s.startswith(prefix)
    
    def redendswith(self, s, suffix):
        """RedCode check if string ends with suffix"""
        return s.endswith(suffix)
    
    def redfind(self, s, substring):
        """RedCode find substring"""
        return s.find(substring)
    
    # Dictionary operations
    def reddict(self, **kwargs):
        """RedCode create dictionary"""
        return dict(kwargs)
    
    def redkeys(self, d):
        """RedCode get dictionary keys"""
        return list(d.keys())
    
    def redvalues(self, d):
        """RedCode get dictionary values"""
        return list(d.values())
    
    def reditems(self, d):
        """RedCode get dictionary items"""
        return list(d.items())
    
    def redget(self, d, key, default=None):
        """RedCode get from dictionary with default"""
        return d.get(key, default)
    
    # Utility functions
    def redrange(self, *args):
        """RedCode range function"""
        return list(range(*args))
    
    def redenumerate(self, iterable):
        """RedCode enumerate function"""
        return list(enumerate(iterable))
    
    def redzip(self, *iterables):
        """RedCode zip function"""
        return list(zip(*iterables))
    
    def redfilter(self, func, iterable):
        """RedCode filter function"""
        return list(filter(func, iterable))
    
    def redmap(self, func, iterable):
        """RedCode map function"""
        return list(map(func, iterable))
    
    def redany(self, iterable):
        """RedCode any function"""
        return any(iterable)
    
    def redall(self, iterable):
        """RedCode all function"""
        return all(iterable)
    
    def redsorted(self, iterable, reverse=False):
        """RedCode sorted function"""
        return sorted(iterable, reverse=reverse)
    
    def redreversed(self, iterable):
        """RedCode reversed function"""
        return list(reversed(iterable))
    
    def parse_line(self, line):
        """Parse a single line of RedCode"""
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            return None
        
        # Handle redexternal imports
        if line.startswith('redexternal ') and line.endswith(';'):
            module_name = line[12:-1].strip()  # Remove 'redexternal ' and ';'
            self.redexternal(module_name)
            # Make module available in variables
            self.variables[module_name] = self.imported_modules[module_name]
            return None
        
        # Handle control structures (if, for, while, etc.) - they don't need semicolons
        control_keywords = ['if ', 'elif ', 'else:', 'for ', 'while ', 'def ', 'class ', 'try:', 'except', 'finally:', 'with ']
        is_control_structure = any(line.startswith(keyword) for keyword in control_keywords)
        
        if is_control_structure:
            return line  # Return as-is for control structures
        
        # Remove semicolon at the end for regular statements
        if line.endswith(';'):
            line = line[:-1]
        else:
            raise SyntaxError(f"Missing semicolon at end of line: {line}")
        
        return line
    
    def execute_line(self, line):
        """Execute a single line of RedCode"""
        try:
            # Convert RedCode to Python and execute
            python_code = self.convert_to_python(line)
            
            # Create execution environment with all functions
            exec_globals = {
                '__builtins__': {
                    'len': len,
                    'int': int,
                    'str': str,
                    'float': float,
                    'type': type,
                    'input': input,
                    'print': print
                }
            }
            
            # Add all methods that start with 'red' from self
            for attr_name in dir(self):
                if attr_name.startswith('red') and callable(getattr(self, attr_name)):
                    exec_globals[attr_name] = getattr(self, attr_name)
            
            # Add variables and imported modules
            exec_globals.update(self.variables)
            exec_globals.update(self.imported_modules)
            
            # Execute the Python code
            exec(python_code, exec_globals, self.variables)
            
        except Exception as e:
            raise RuntimeError(f"Error executing line '{line}': {str(e)}")
    
    def convert_to_python(self, redcode_line):
        """Convert RedCode line to Python"""
        # RedCode is basically Python with red* functions
        # Just return the line as-is since we provide the red* functions
        return redcode_line
    
    def run_file(self, filename):
        """Run a RedCode file"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line_num, line in enumerate(lines, 1):
            try:
                parsed_line = self.parse_line(line)
                if parsed_line is not None:
                    self.execute_line(parsed_line)
            except Exception as e:
                print(f"Error on line {line_num}: {e}")
                sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python redcode.py <filename.red>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not filename.endswith('.red'):
        print("Error: File must have .red extension")
        sys.exit(1)
    
    interpreter = RedCodeInterpreter()
    
    try:
        interpreter.run_file(filename)
    except Exception as e:
        print(f"RedCode Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()