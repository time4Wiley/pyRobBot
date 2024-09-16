#!/usr/bin/env python
# -*- coding: utf-8 -*-

__filename__ = "start_server.py"

__author__ = "Sun Wei"
__copyright__ = "Copyright (C) 2023 Sun Wei"
__license__ = "Private"
__version__ = "1.0"


def main():
    import os
    import sys
    
    # get python path
    python_path = os.path.abspath(sys.executable)
    
    # get streamlit path
    script_streamlit = os.path.join(os.path.dirname(python_path), r'streamlit')
    
    # my script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_webserver = os.path.join(current_dir, r'rob.py')
    
    # Here is the magic to execute  "streamlit run WebServer.py"
    sys.argv = [script_streamlit, "run", script_webserver]
    exec(open(script_streamlit).read())


if __name__ == "__main__":
    main()
