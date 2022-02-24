"""Example of a function that searches through a list"""

def main() -> None:



#Define a function named comtains
#Two parameters:
#   1. needle - the string we are searching for
#   2. haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:

#Algorithm:
#   for each item in a ahystack
#   test if it is equal to the needle
    #if so, then return true
    for item in haystack:
        if item == needle:
            return True

        #returns true if needle in haystack, false otherwise
    return False

if __name__ == "__main__":
    """We do this because we can run this as a one program like normal, and can import functions we want in our repl"""
    main()
