from analyzer.git_reader import GitReader
from analyzer.coupling_detector import CouplingDetector

reader = GitReader("./data/flask")

commits = reader.get_commit_files()

print(f"Total commits: {len(commits)}")

detector = CouplingDetector(commits)

couplings = detector.detect_couplings(min_coupling_count=5)

print("\nTop hidden evolutionary couplings:\n")

for item in couplings[:20]:
    print(
        item["file_a"],
        "<-->",
        item["file_b"],
        "| changed together:",
        item["co_change_count"],
        "times",
    )