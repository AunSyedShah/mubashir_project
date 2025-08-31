#!/usr/bin/env python3
import os
import re

def fix_paths_in_file(filepath):
    """Fix absolute paths in HTML files to use relative paths"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Determine if this is in a subdirectory (aboutdogs)
        is_subdirectory = 'aboutdogs' in filepath
        prefix = '../' if is_subdirectory else ''
        
        # Fix image paths
        content = re.sub(r'src="/img/', f'src="{prefix}img/', content)
        content = re.sub(r'href="/CSS/', f'href="{prefix}CSS/', content)
        
        # Fix navigation links
        if is_subdirectory:
            content = re.sub(r'href="/([^"]+\.html)"', r'href="../\1"', content)
            content = re.sub(r'href="/aboutdogs/', 'href="', content)
        else:
            content = re.sub(r'href="/([^"]+\.html)"', r'href="\1"', content)
            content = re.sub(r'href="/aboutdogs/', 'href="aboutdogs/', content)
        
        # Fix broken links in food&nutrition.html
        if 'food&nutrition.html' in filepath:
            content = content.replace('href="/treats.html"', 'href="treats.html"')
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed paths in: {filepath}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    project_root = "/workspaces/mubashir_project/patrona-puppy-project-master"
    
    # Process all HTML files in the root directory
    for filename in os.listdir(project_root):
        if filename.endswith('.html'):
            fix_paths_in_file(os.path.join(project_root, filename))
    
    # Process all HTML files in the aboutdogs directory
    aboutdogs_dir = os.path.join(project_root, 'aboutdogs')
    if os.path.exists(aboutdogs_dir):
        for filename in os.listdir(aboutdogs_dir):
            if filename.endswith('.html'):
                fix_paths_in_file(os.path.join(aboutdogs_dir, filename))

if __name__ == "__main__":
    main()
