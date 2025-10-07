from summarizer import Summarizer

def main():
    # Read input from file
    with open("sample.txt", "r", encoding="utf-8") as f:
        text = f.read()

    summarizer = Summarizer()
    summary_sentences = summarizer.summarize(text, num_sentences=3)

    # Write summary to file
    with open("output/summary.txt", "w", encoding="utf-8") as f:
        for sentence in summary_sentences:
            f.write(sentence.strip() + "\n")

    # Optional: print summary to console
    print("\n--- Summary Written to output/summary.txt ---")
    for sentence in summary_sentences:
        print(sentence.strip())

if __name__ == "__main__":
    main()

