from git import Repo


class GitReader:
    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def get_commit_files(self):
        commit_data = []

        for commit in self.repo.iter_commits():
            files = []

            if commit.parents:
                parent = commit.parents[0]

                diffs = parent.diff(commit)

                for diff in diffs:
                    if diff.a_path:
                        files.append(diff.a_path)

            commit_data.append(
                {
                    "hash": commit.hexsha,
                    "message": commit.message.strip(),
                    "files": files,
                }
            )

        return commit_data