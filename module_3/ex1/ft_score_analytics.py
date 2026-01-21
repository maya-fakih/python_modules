import sys


def main():
    scores = []
    i = 1

    print("=== Player Score Analytics ===")
    try:
        while i < len(sys.argv):
            scores.append(int(sys.argv[i]))
            i += 1

        if (len(scores) == 0):
            print("No scores provided. Usage: python3 \
                  ft_score_analytics.py <score1> <score2> \
                  ...")

        else:
            print(f"Scored Processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Avarage score: {0.0 + (sum(scores) / len(scores))}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")

    except Exception:
        print("Error your variables failed to convert to int")


if __name__ == '__main__':
    main()
