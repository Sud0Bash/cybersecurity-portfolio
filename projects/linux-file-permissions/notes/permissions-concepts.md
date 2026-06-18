# Permissions Concepts Notes

## Permission Characters

Linux permission strings show who can read, write, or execute a file or directory.

Example:

```text
-rw-r--r--
```

Breakdown:

- `-` means regular file.
- `rw-` means the owner can read and write.
- `r--` means the group can read.
- `r--` means others can read.

## Files vs. Directories

Permissions behave differently for files and directories:

- File read permission allows reading file contents.
- File write permission allows modifying file contents.
- File execute permission allows running a file as a program or script.
- Directory read permission allows listing directory contents.
- Directory write permission allows creating, deleting, or renaming entries.
- Directory execute permission allows entering or traversing the directory.

## `chmod` Basics

Symbolic `chmod` changes use:

- `u` for user/owner.
- `g` for group.
- `o` for other.
- `a` for all.
- `+` to add a permission.
- `-` to remove a permission.
- `r`, `w`, and `x` for read, write, and execute.

Examples:

```bash
chmod o-w project_k.txt
chmod g-x drafts
chmod u-w,g-w,g+r .project_x.txt
```

## Review Checklist

- Run `ls -la` to include hidden files.
- Check whether others have write access.
- Check whether group access is required.
- Review directories separately from regular files.
- Apply the smallest permission change needed.
- Run `ls -la` again to verify the result.

## Security Takeaway

File permissions are a basic but important access-control layer. Reviewing them helps reduce unnecessary access and supports least privilege, especially in shared directories.
