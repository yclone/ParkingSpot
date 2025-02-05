import os
import shutil

def cleanup():
    patterns = [
        '__pycache__',
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '.Python',
        'build',
        'develop-eggs',
        'dist',
        '*.egg-info',
        '.coverage',
        '.pytest_cache'
    ]
    
    for pattern in patterns:
        for root, dirs, files in os.walk('.'):
            for item in dirs + files:
                if pattern in item:
                    path = os.path.join(root, item)
                    if os.path.isfile(path):
                        os.remove(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                    print(f"Removed: {path}")

if __name__ == "__main__":
    cleanup()