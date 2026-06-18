# Linux File Permissions Review

## Project Overview

This project documents a beginner-level Linux file-permissions review using sanitized lab screenshots and original Markdown documentation. The goal is to show that I understand how Linux permission strings work, how to inspect permissions with `ls -la`, and how `chmod` can reduce unnecessary access.

The public evidence for this project is the original Markdown report and sanitized screenshots.

## Scenario Summary

A lab directory contained several project files, a hidden file, and a drafts directory. I reviewed the permissions, identified entries with broader access than needed, and adjusted permissions to better match least-privilege expectations.

This was a local learning exercise, not professional Linux administration or production system hardening.

## Skills Demonstrated

- Reading Linux permission strings.
- Using `ls -la` to inspect files, hidden files, directories, owners, and groups.
- Understanding user, group, and other permission categories.
- Using `chmod` to remove unnecessary write or execute access.
- Explaining least privilege in a practical file-permissions context.
- Documenting command-line evidence with sanitized screenshots.

## Commands and Concepts Used

- `cd` to move into the lab project directory.
- `ls -la` to show detailed file listings, including hidden files.
- `chmod o-w <file>` to remove write permission from others.
- `chmod u-w,g-w,g+r <file>` to adjust user and group access on a hidden file.
- `chmod g-x <directory>` to remove group execute permission from a directory.
- Linux permission categories: user, group, and other.
- Linux permission types: read, write, and execute.

## Screenshot Evidence

| Screenshot | What it shows |
| --- | --- |
| [permissionssc.png](screenshots/permissionssc.png) | Initial `ls -la` review of project files, hidden file, and drafts directory. |
| [permissionssc2.png](screenshots/permissionssc2.png) | `chmod o-w project_k.txt` removing write access for others. |
| [permissionssc3.png](screenshots/permissionssc3.png) | Additional permission adjustment on the hidden file `.project_x.txt`. |
| [permissionssc4.png](screenshots/permissionssc4.png) | Final permission checks and `chmod g-x drafts` removing group execute access from the drafts directory. |

## File Permission Findings

- One regular file allowed write access for others, which was broader than needed.
- The hidden file had permissions that needed adjustment to better limit write access while preserving expected read access.
- The drafts directory allowed group execute access, which controls whether group members can enter or traverse the directory.
- Several project files already had reasonable read/write permissions for the lab scenario.

## Changes and Recommendations

- Removed write access for others from a project file.
- Adjusted permissions on the hidden file to reduce unnecessary write access.
- Removed group execute access from the drafts directory.
- Recommended reviewing file permissions regularly when files are shared across users or groups.
- Recommended applying least privilege: give users only the access required for the task.

## Report

- [Linux File Permissions Review](reports/linux-file-permissions-review.md)
- [Permissions Concepts Notes](notes/permissions-concepts.md)

## Ethical and Sanitization Note

This project uses a simulated local lab environment and sanitized screenshots. It does not include real company systems, private production files, credentials, or sensitive user data.

The public documentation is written in original wording and focuses on concepts learned, commands used, observations, and safe recommendations.

## Lessons Learned

- `ls -la` is useful because it shows hidden files, owners, groups, and permission strings.
- A permission string can quickly show whether access is too broad.
- `chmod` can remove access without changing file ownership.
- Directory execute permission matters because it controls traversal.
- Least privilege is easier to apply when permissions are reviewed file by file.
