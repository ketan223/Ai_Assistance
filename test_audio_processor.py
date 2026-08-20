import sys

from utils.audio_processor import process_input


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=ysz5S6PUM-U"

    print(f"Testing audio processor with URL: {url}")
    chunks = process_input(url)

    print(f"Chunk count: {len(chunks)}")
    for chunk in chunks:
        print(chunk)


if __name__ == "__main__":
    main()
