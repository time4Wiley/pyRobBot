#!/usr/bin/env python
# -*- coding: utf-8 -*-

__filename__ = "WebServer.py.py"

__author__ = "Sun Wei"
__copyright__ = "Copyright (C) 2023 Sun Wei"
__license__ = "Private"
__version__ = "1.0"


def main():
    import pandas as pd
    import streamlit as st

    df = pd.DataFrame({
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40]
    })

    st.dataframe(df)


if __name__ == "__main__":
    main()
