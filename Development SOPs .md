# Development SOPs

# Development Process SOP

This document outlines the standard operating procedure (SOP) for developing new requirements in the 'epic<#>-<name>' branch, integrating developments to the 'Testing' branch, testing, and updating the main branch.

## Pre-requisites

- Familiarity with Git and the project repository.
- Access to the project repository.

## Development Process

### Step 1: Creating and Updating the 'epic<#>-<name>' Branch

1.1. Create a new branch for the development of a specific requirement or feature.

```bash
git checkout main
git pull origin main
git checkout -b epic<#>-<name>

```

1.2. Develop the new requirements within this branch.

1.3. Periodically update the branch with changes from the 'main' branch to ensure you are working with the latest code.

```bash
git checkout main
git pull origin main
git checkout epic<#>-<name>
git merge main

```

### Step 2: Integration to the 'Testing' Branch

2.1. After completing development and ensuring your code works as expected, it's time to integrate the changes into the 'Testing' branch.

```bash
git checkout Testing
git pull origin Testing
git merge epic<#>-<name>

```

2.2. Address any merge conflicts, if they occur.

2.3. Commit your changes after merging.

```bash
git commit -m "Merged epic<#>-<name> into Testing"

```

### Step 3: Testing in the 'Testing' Branch

3.1. Testers will now move 'test_*' files from the 'Testing' branch into the main directory.

3.2. Perform testing in the 'Testing' branch with the moved 'test_*' files.

3.3. If issues are identified during testing, they should be addressed in the 'epic<#>-<name>' branch.

### Step 4: Updating the Backup Branch

4.1. Before making any significant changes, create a backup branch.

```bash
git checkout -b backup

```

4.2. After testers have completed testing, update the backup branch with the latest changes.

```bash
git checkout Testing
git pull origin Testing
git checkout backup
git merge Testing

```

### Step 5: Moving 'test_*.xxx' Files to 'TestFiles' Folder

5.1. Move 'test_*.xxx' files from the 'Testing' branch into the 'TestFiles' folder.
5.2 example - all test for features from E2 to be renamed test_E2xx.py and pushed to TestFilesE2 folder. and all new test files for all new features of test_E3xx.py to be pushed to TestFilesE3

```bash
mkdir TestFileE#
mv test_*.xxx TestFiles/
```

5.3. Commit the changes.

```bash
git add .
git commit -m "Moved test files to TestFiles folder"

```

### Step 6: Updating the 'epic<#>-<name>' Branch with Tests

6.1. Move 'TestFiles' folder contents into the 'epic<#>-<name>' branch.

```bash
git checkout epic<#>-<name>
git checkout Testing -- TestFiles/

```

6.2. Commit the changes.

```bash
git add .
git commit -m "Updated epic<#>-<name> with tests in TestFiles folder"

```

### Step 7: Updating the 'main' Branch

7.1. The Scrum Master will update the 'main' branch with the final commit of 'epic<#>-<name>'.

```bash
git checkout main
git pull origin main
git merge epic<#>-<name>

```

7.2. Resolve any conflicts if they occur.

7.3. Commit and push the changes to the 'main' branch.

```bash
git commit -m "Merged epic<#>-<name> with final tests into main"
git push origin main

```

## Conclusion

Following this SOP will ensure a structured and efficient development process while maintaining code quality and testing rigor.