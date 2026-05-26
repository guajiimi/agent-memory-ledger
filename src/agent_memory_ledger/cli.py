import argparse
import json
from .core import analyze, load, save

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    parser.add_argument("--out", "-o")
    args = parser.parse_args(argv)
    result = analyze(load(args.input_json))
    text = json.dumps(result, indent=2)
    if args.out:
        save(result, args.out)
    print(text)

if __name__ == "__main__":
    main()
