# RedCode Demo - External Modules with Auto-Wrapping
redprint("=== RedCode External Module Demo ===");

# JSON Module
redexternal json;
redprint("JSON module imported with red-wrappers!");

# JSON processing
json_data = redloads('{"name": "RedCode", "version": 1.0, "features": ["auto-wrapping", "syntax-highlighting"]}');
redprint("Parsed JSON:", json_data);
redprint("Name:", json_data["name"]);
redprint("Features:", json_data["features"]);

json_string = reddumps(json_data);
redprint("JSON String:", json_string);

# Time Module
redexternal time;
redprint("Time module imported with red-wrappers!");

current_time = redtime();
redprint("Current timestamp:", current_time);

redprint("Sleeping for 1 second...");
redsleep(1);
redprint("Done sleeping!");

# Random Module  
redexternal random;
redprint("Random module imported with red-wrappers!");

random_number = redrandint(1, 100);
redprint("Random number (1-100):", random_number);

choices = redlist("apple", "banana", "cherry", "date", "elderberry");
random_choice = redchoice(choices);
redprint("Random choice from fruits:", random_choice);

# Multiple random numbers
random_numbers = redlist();
redappendlist(random_numbers, redrandint(1, 10));
redappendlist(random_numbers, redrandint(1, 10));
redappendlist(random_numbers, redrandint(1, 10));
redappendlist(random_numbers, redrandint(1, 10));
redappendlist(random_numbers, redrandint(1, 10));
redprint("5 random numbers:", random_numbers);

# Math Module (already available)
redexternal math;
redprint("Math module available!");
redprint("Pi:", math.pi);
redprint("Square root of random number:", redsqrt(random_number));
redprint("Sine of Pi/2:", math.sin(math.pi / 2));

# Base64 Module
redexternal base64;
redprint("Base64 module imported!");

text = "Hello RedCode!";
encoded = redb64encode(text.encode());
redprint("Original text:", text);
redprint("Base64 encoded:", encoded);

# Combined String and List Operations
redprint("=== String & List Operations ===");
sentence = "RedCode makes programming simple and fun";
words = redsplit(sentence);
redprint("Original sentence:", sentence);
redprint("Words:", words);
redprint("Word count:", redlen(words));

# Reverse words and join back
redreverse(words);
reversed_sentence = redjoin(" ", words);
redprint("Reversed sentence:", reversed_sentence);

redprint("=== Demo Complete! ===");