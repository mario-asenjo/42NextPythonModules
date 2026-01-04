"""
This program demonstrates how to properly handle standard streams
"""
import sys


def retrieve_stdin(message: str) -> str:
    """Function in charge of handling stdin"""
    sys.stdout.write("Input Stream active. " + message)
    return sys.stdin.readline()[:-1]


def process_status_report(id: str, s_report: str) -> None:
    """Function in charge of processing the report"""
    sys.stdout.write(
        "\n{[}STANDARD{]} Archive status from " + id + ": " + s_report
    )
    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication channels verified"
    )
    sys.stdout.write(
        "{[}STANDARD{]} Data transmission complete\n"
    )


def main() -> None:
    """Main function that calls functions to simulate subject"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id: str = retrieve_stdin("Enter archivist ID: ")
    status_report: str = retrieve_stdin("Enter status report: ")
    process_status_report(archivist_id, status_report)
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
