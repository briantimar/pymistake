""" List TODOs"""
import argparse

priorities = {1 : "Worth doing if you have the time", 
              2 : "Pretty urgent, but it still works", 
              3 : "Might brick your machine", 
              4 : "National security"}

#### salt to taste
priorities_profane = {1 : "Kinda important", 
                    2 : "Shitty but it still works", 
                    3 : "jesus man just fix this", 
                    4 : "fucking fuck"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List TODOs in the given file")
    parser.add_argument("filename", type=str, help="Source file to read.")
    parser.add_argument("-profane", action="store_true", help="Use profanity in summaries.")
    parser.add_argument("-windowsize", type=int, default=5, help="Number of lines per window.")
    args = parser.parse_args()
    source = args.filename

    snippet_size = args.windowsize
    if args.profane:
        priorities = priorities_profane

    window = []
    window_priority = 0
    startline = 0

    def flush():
        global window
        print(f"In {source}, line {startline}: {priorities[window_priority]}")
        print("".join(window))
        print("-"*30)
        window = []


    print(f"Todo's in {source}:\n" + "="*30)
    tasks = [list() for _ in range(len(priorities))]
    windowct = 0

    with open(source) as f:
        for linenum, ln in enumerate(f.readlines()):
            ct = ln.count("TODO")
            if len(window) > 0:
                if len(window) == snippet_size or ct > 0:
                    #flush the window
                    flush()
                else:
                    window.append(ln)
            if ct > 0:
                assert len(window) == 0
                window_priority = ct
                startline = linenum + 1
                window.append(ln) 
