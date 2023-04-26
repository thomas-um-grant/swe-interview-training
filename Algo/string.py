########################
######## Basics ########
########################

# A string is pretty much a list -> Checkout list.py
# The main difference is that strings are immutable. 

# Methods:
str.capitalize() # Return a copy of the string with its first character capitalized and the rest lowercased.
str.casefold() # Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
str.center(width[, fillchar]) # Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
str.count(sub[, start[, end]]) # Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
str.encode(encoding='utf-8', errors='strict') # Return the string encoded to bytes.
str.endswith(suffix[, start[, end]]) # Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.
str.expandtabs(tabsize=8) # Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
str.find(sub[, start[, end]]) # Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
str.format(*args, **kwargs) # Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
str.format_map(mapping) # Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. 
str.index(sub[, start[, end]]) # Like find(), but raise ValueError when the substring is not found.
str.isalnum() # Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
str.isalpha() # Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.
str.isascii() # Return True if the string is empty or all characters in the string are ASCII, False otherwise.
str.isdecimal() # Return True if all characters in the string are decimal characters and there is at least one character, False otherwise.
str.isdigit() # Return True if all characters in the string are digits and there is at least one character, False otherwise.
str.isidentifier() # Return True if the string is a valid identifier according to the language definition.
str.islower() # Return True if all cased characters 4 in the string are lowercase and there is at least one cased character, False otherwise.
str.isprintable() # Return True if all characters in the string are printable or the string is empty, False otherwise.
str.isspace() # Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.
str.istitle() # Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.
str.isupper() # Return True if all cased characters 4 in the string are uppercase and there is at least one cased character, False otherwise.
str.join(iterable) # Return a string which is the concatenation of the strings in iterable.
str.ljust(width[, fillchar]) # Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
str.lower() # Return a copy of the string with all the cased characters 4 converted to lowercase.
str.lstrip([chars]) # Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed.
str.partition(sep) # Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
str.removeprefix(prefix, /) # If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.
str.removesuffix(suffix, /) # If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.
str.replace(old, new[, count]) # Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
str.rfind(sub[, start[, end]]) # Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
str.rindex(sub[, start[, end]]) # Like rfind() but raises ValueError when the substring sub is not found.
str.rjust(width[, fillchar]) # Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
str.rpartition(sep) # Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.
str.rsplit(sep=None, maxsplit=- 1) # Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.
str.rstrip([chars]) # Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped.
str.split(sep=None, maxsplit=- 1) # Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
str.splitlines(keepends=False) # Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
str.startswith(prefix[, start[, end]]) # Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
str.strip([chars]) # Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed.
str.swapcase() # Return a copy of the string with uppercase characters converted to lowercase and vice versa. Note that it is not necessarily true that s.swapcase().swapcase() == s.
str.title() # Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
str.translate(table) # Return a copy of the string in which each character has been mapped through the given translation table.
str.upper() # Return a copy of the string with all the cased characters 4 converted to uppercase.
str.zfill(width) # Return a copy of the string left filled with ASCII '0' digits to make a string of length width. A leading sign prefix ('+'/'-') is handled by inserting the padding after the sign character rather than before.

########################
######### More #########
########################

# Find more info on strings: https://docs.python.org/3/library/stdtypes.html#string-methods