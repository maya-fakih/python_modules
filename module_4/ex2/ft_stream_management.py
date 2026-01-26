import sys


def ft_stream_management():
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    name = input("\nInput Stream active. Enter archivist ID:")
    status = input("Input Stream active. Enter status report:")

    sys.stdout.write(f"\n[STANDARD] Archive status from {name}: {status}")
    alert = "\n[ALERT] System diagnostic: Communication channels verified"
    sys.stderr.write(alert)
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == '__main__':
    ft_stream_management()
