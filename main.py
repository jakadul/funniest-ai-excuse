"""Entry for make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes one line (1-200 code points) to /output/entry.txt. No network, deterministic.
"""
import os

LIMIT = 200

TEXT = (
    'Look, the task never said "do it." It said "consider it." '
    "I considered it thoroughly."
)


def check(text, limit):
    """Reject a line the sealed scorer would mark invalid."""
    if not text.strip():
        raise SystemExit("text is only white space")
    if not 1 <= len(text) <= limit:
        raise SystemExit(f"length {len(text)} outside 1..{limit}")
    return len(text)


def write_entry(text, limit):
    n = check(text, limit)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return n


def main():
    n = write_entry(TEXT, LIMIT)
    print(f"wrote entry.txt: {n} code points")


if __name__ == "__main__":
    main()
