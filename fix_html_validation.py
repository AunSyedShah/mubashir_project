#!/usr/bin/env python3
import os
import re

def fix_img_attributes(filepath):
    """Fix invalid HTML img attributes"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix incorrect width attribute syntax (width=20% should be width="20%")
        content = re.sub(r'width=(\d+%)', r'width="\1"', content)
        
        # Fix img tags without proper closing
        content = re.sub(r'<img([^>]+)\/>', r'<img\1>', content)
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed img attributes in: {filepath}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    project_root = "/workspaces/mubashir_project/patrona-puppy-project-master"
    
    # Process all HTML files in the root directory
    for filename in os.listdir(project_root):
        if filename.endswith('.html'):
            fix_img_attributes(os.path.join(project_root, filename))
    
    # Process all HTML files in the aboutdogs directory
    aboutdogs_dir = os.path.join(project_root, 'aboutdogs')
    if os.path.exists(aboutdogs_dir):
        for filename in os.listdir(aboutdogs_dir):
            if filename.endswith('.html'):
                fix_img_attributes(os.path.join(aboutdogs_dir, filename))

if __name__ == "__main__":
    main()
