import sys
sys.path.append('../')

from agents.generator import Generator
from core.comms import FixItem


def main():
    gen = Generator()
    goal = "Write a python program that is capable of checking if a user-inputted string is a palindrome."
    past_code = ""
    fix_items = []
    draft = gen.generate(goal=goal, past_code=past_code, fix_items=fix_items, iteration=0)

    assert isinstance(draft.code, str) and len(draft.code.strip()) > 0
    assert isinstance(draft.applied_fixes, list)
    assert isinstance(draft.notes, str)

    print(" -- CODE -- ")
    print(draft.code)
    print(" -- APPLIED FIXES -- ")
    print(draft.applied_fixes)
    print(" -- NOTES -- ")
    print(draft.notes)

if __name__ == "__main__":
    main()
