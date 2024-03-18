#!/bin/bash

# Step 1: Create a new branch
git checkout -b backup_branch

# Step 2: Checkout the commit
git checkout 3af4c4749cc3beb067233b3f5036f95835955c64

# Step 3: Create a directory to store the backup
mkdir backup

# Step 4: Copy all files to the backup directory
cp -r . backup/

# Optional: You can switch back to your original branch if needed
# git checkout <original_branch_name>

echo "Backup completed. Files are stored in the 'backup' directory."
