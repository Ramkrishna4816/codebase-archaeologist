from itertools import combinations
from collections import defaultdict


class CouplingDetector:
    def __init__(self, commit_data):
        self.commit_data = commit_data

    def detect_couplings(self, min_coupling_count=3):
        coupling_counts = defaultdict(int)

        for commit in self.commit_data:
            files = commit["files"]

            unique_files = list(set(files))

            if len(unique_files) < 2:
                continue

            for file_a, file_b in combinations(sorted(unique_files), 2):
                coupling_counts[(file_a, file_b)] += 1

        results = []

        for (file_a, file_b), count in coupling_counts.items():
            if count >= min_coupling_count:
                results.append(
                    {
                        "file_a": file_a,
                        "file_b": file_b,
                        "co_change_count": count,
                    }
                )

        results.sort(key=lambda x: x["co_change_count"], reverse=True)

        return results