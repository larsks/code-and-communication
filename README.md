# Git best practices

A fantastic quote:

> Likewise, computers don’t care what a commit message looks like, but it
> affects the humans interacting with the codebase. Good programmers write
> commit messages that humans can understand.
> 
> To echo my earlier post, how we commit code can be as important as what code
> we commit. The code we write will be changed over time, but the commit
> message we write will live forever as a snapshot of our intent, what we
> thought the system should do and why.
> 
> Our commit messages are our love letters to the future maintainers of our
> code.

(from https://www.simplethread.com/git-commit-message-101/)


- Your development environment
  - Use an editor that can perform live syntax checking

  - Configure pre-commit checks
    - https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

  - Submitting changes with syntax errors or other trivial issues does not
    respect the time of the reviewers (and can end up delaying getting your
    code merged)

- Ch-ch-ch-changes
  - Changes should be *isolated*
    - This makes it possible to revert commits
    - Makes it more likely your code will merge
    - Learning about `git add -p`

  - Smaller is better

  - Commit log should tell a story

- Writing good commit messages

  - Subject line should be descriptive by itself

  - Commit message body should explain why the changes were necessary and
    how you addressed the problem.

    - Should not describe what files you changed (this is why we have
      `git log`).

    - "Write a meaningful summary"

  - Examples of good/not so good commit messages

    - Some good examples

      - https://github.com/containers/podman/commit/7e30531f20b8c367aad81454abda8505a0d9962a
      - https://github.com/ansible/ansible/commit/9142be2f6cabbe6597c9254c5bb9186d17036d55
      - https://github.com/kubernetes/kubernetes/pull/107248/commits/a82c275df54a636a48e7953e0ff245cd877cec55

    - Don't be afraid to link to supporting documentation in your commits:

      - https://github.com/CCI-MOC/moc-apps/commit/57bff2cefbcdb43646130d906910a7bd824f1fbf

    - Not so good:

      - "Fixed some errors"
      - "Respond to review comments"
      - "Remove useless lines"

  - Common conventions
    - Separate subject from body with a blank line
    - Limit the subject line to 50 characters (-ish)
    - Capitalize the subject line
    - Do not end the subject line with a period
    - Use the imperative mood in the subject line ("if applied, this commit
      will...")
    - Wrap the body at 72 characters


- Rewriting history (for great justice!)

  - Typos, syntax errors, etc, normally don't need their own commits.
  - Update most recent commit: `git commit --amend`
  - Update older commits: `git rebase -i`
    - Editing commit messages
    - Reordering commits
    - Squashing
    - Fixups

- Making good pull requests

  - Commits in a pull request should be tightly coupled
  - Your pull request does not need to resemble your local commit history
    (see above re: reordering, squashing, etc)

- References

  - https://www.simplethread.com/git-commit-message-101/
  - https://google.github.io/eng-practices/review/developer/cl-descriptions.html
  - https://www.kubernetes.dev/docs/guide/pull-requests
