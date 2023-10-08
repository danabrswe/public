# assume that module_one is being run when the order of code execution is explained in module_one and module_two

import module_two   # order 1. then over to module_two because of the import.

if __name__ == "__main__":                  # order 5. module_one finishes it's own module, running directly
    print("running module_one directly")
else:
    print("running module_one indirectly")  # order 3. module_one is being run through module_two's import.
                                            # here it continues after module_one's import statement to
                                            # prevent inifinite loop of imports.
                                            # module_two's import of module_one is now done.