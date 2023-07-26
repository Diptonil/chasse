# Version 1.1.0

## Enhancements

- [#5](https://github.com/Diptonil/chasse/issues/5): Add additional option for deciding resultant file names: `-l`.


## Bug Fixes

- [#12](https://github.com/Diptonil/chasse/issues/12): Fix missing arguments with optionals like `-p` with an error message (in case argument not provided).
- [#10](https://github.com/Diptonil/chasse/issues/10): Fix parent declarations system. Single-line comments and line breaks before and between the parent declaration are now permitted.


## Additional Notes

- Imports made more readable.
- [#14](https://github.com/Diptonil/chasse/issues/14): Docker image build released.


# Version 1.0.0

## Enhancements

- [#1](https://github.com/Diptonil/chasse/issues/1): Fix rogue indentations in the resultant HTML file.


## Bug Fixes

None.


## Additional Notes

- Official release for Windows and Linux systems.
- Formal specification of conventions established.
- Formal draft of documentation started.


# Version 0.2.1

## Enhancements

- Minor refactoring and standardization of code.
- [#2](https://github.com/Diptonil/chasse/issues/2): Add Black formatter.


## Bug Fixes

None.


## Additional Notes

None.


# Version 0.2.0

- [#3](https://github.com/Diptonil/chasse/issues/3): Improved CLI error and success messages.
- Add additional option of enabling low-level verbose logs: `-l`.
- Change extensions of the parent and chasse files from `.html` to `.chasse.html` to avoid confusion between resultant files and enforce a standard.


## Bug Fixes

None.


## Additional Notes

None.


# Version 0.1.0

## Additional Notes

- Initial deation and execution of design.
- Basic child HTML file parsing to get required components.
- Parsing parent HTML file for extracting components.
- Generation of resultant HTML files with the components.
