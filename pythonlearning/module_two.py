import module_one       # order 2. then back to module_one again because of another import.

if __name__ == "__main__":
    print("running module_two directly")
else:
    print("running module_two indirectly")  # order 4. module_one finishes import of module_two by
                                            # running module_two indirectly.
                                            # module_one's import of module_two is now done.