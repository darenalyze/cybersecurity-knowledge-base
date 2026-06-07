# Keylogger

## Goal
- [x] Still works with other program
- [ ] Process hidden
- [x] Live output will pass on file
- [ ] All proper keys detection 
- [ ] Mouse position detection
- [ ] Time and date when the key is detected

## Updates
- **6/7/2026:**
  - New style at keylog.txt and improved readability of output
    - `key.enter` to `/(enter)`
    - `key.backspace` to `/(backspace)`
    - `key.space` to `" "`
  - Backspace key added to special key list

## Process
- I searched what library I will use at this one and i found out that `pynput` is perfect for this one.
- Source of how to use this `pynput` library: https://pypi.org/project/pynput/
- Also I use `os` library to know where the result or live input of the file will be as default
- The press recording logic works like this:
  - all letters input will append in one list and if one of these key is pressed, the list will be uploaded in file:
    - Windows key, Space key, Enter key, Esc key
  - I decided to use this to reduce lag spike per key so it can capture every key accurately and support low-end systems

## Errors Encountered
- Error 1 Pylance(reportMissingModuleSource)
> **Cause:** I thought "pynput" is in python standard library so I imported the "pynput" module that does not yet downloaded
> **Resolution:** I install the module using integrated terminal in vsCode and i typed "python -m pip install pynput"

- Error 2 TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
> **Cause:** Adding up the NoneType and StringType. 
> **Resolution:** Adding Exception Handling try and except.

- Error 3 UnboundLocalError: cannot access local variable 'result' where it is not associated with a value
> **Cause:** Try to use the variable before it's defined `result = result+key`
> **Resolution:** I initialized `result` as an empty string and simplified the logic to concatenate all keys in the list.

## Notes
- It is nice to know that in python adding the NoneType to StringType will return error. I expect it will return only the string 
