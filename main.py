import sys
import os

# Add the Modules folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

import login # type: ignore
import home # type: ignore

def main():
    login.main()
    home.main()

if __name__ == "__main__":
    main()
