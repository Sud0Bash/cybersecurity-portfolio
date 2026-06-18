# Linux File Permissions Review

## Objective

Review file and directory permissions in a Linux lab directory, identify permissions that are broader than needed, and document safe adjustments using original portfolio-ready wording.

## How Linux Permission Strings Work

Linux file listings show permissions in a 10-character string such as:

```text
-rw-r--r--
drwx--x---
```

The first character identifies the file type:

- `-` means a regular file.
- `d` means a directory.

The next nine characters are grouped into three sets:

| Position | Meaning |
| --- | --- |
| Characters 2-4 | Permissions for the user/owner |
| Characters 5-7 | Permissions for the group |
| Characters 8-10 | Permissions for others |

Each permission set can include:

- `r` for read.
- `w` for write.
- `x` for execute or directory traversal.
- `-` when that permission is not granted.

## What `ls -la` Shows

The command `ls -la` shows a detailed listing of all entries in a directory, including hidden files. In this lab, it showed:

- Permission strings for each file and directory.
- Link counts.
- File owner.
- Group owner.
- File size.
- Last modified timestamp.
- File and directory names.
- Hidden files such as `.project_x.txt`.

This output was useful because it made it possible to compare regular files, hidden files, and directories in one view.

## User, Group, and Other Permissions

Linux permissions are split into three access categories:

- **User:** the owner of the file or directory.
- **Group:** users who belong to the assigned group.
- **Other:** everyone else on the system.

In a security review, the `other` category needs careful attention because it can grant access more broadly than intended. Group permissions also matter when multiple users share a lab or project directory.

## Commands Used

### Review current permissions

```bash
ls -la
```

This command was used before and after changes to verify the current permissions.

### Remove write access from others

```bash
chmod o-w project_k.txt
```

This command removed write permission from the `other` category on `project_k.txt`. The reason was to prevent users outside the owner/group from modifying the file.

### Adjust hidden file permissions

```bash
chmod u-w,g-w,g+r .project_x.txt
```

This command adjusted permissions on the hidden file `.project_x.txt`. The goal was to reduce unnecessary write access while allowing group read access where appropriate for the lab scenario.

### Remove group directory traversal

```bash
chmod g-x drafts
```

This command removed group execute permission from the `drafts` directory. On directories, execute permission controls whether a user can enter or traverse the directory.

## Findings

| Item reviewed | Observation | Action |
| --- | --- | --- |
| `project_k.txt` | Other users had write access. | Removed write permission for others. |
| `.project_x.txt` | Hidden file permissions needed tighter control. | Adjusted owner/group permissions with `chmod`. |
| `drafts/` | Group execute permission allowed traversal. | Removed group execute permission. |
| Other project files | Permissions appeared reasonable for the lab scenario. | No change documented. |

## Why Least Privilege Matters

Least privilege means granting only the access needed to complete a task. In file-permissions work, this helps reduce accidental changes, unauthorized reads, and unnecessary access paths.

For this lab, least privilege meant:

- Removing write access from users who did not need it.
- Checking hidden files instead of only visible files.
- Reviewing directory permissions separately from file permissions.
- Verifying changes with `ls -la` after running `chmod`.

## What I Learned

- Permission strings are compact but readable once broken into user, group, and other sections.
- Hidden files can carry important permissions and should be included in reviews.
- `chmod` can make precise permission changes without replacing the whole permission set.
- Directory execute permission is different from file execute permission and affects traversal.
- Screenshots are useful evidence when they show both the command and the before/after output.

## Limitations

This was a beginner lab using simulated files and sanitized screenshots. It does not represent production Linux administration, enterprise access review, or formal system hardening.
