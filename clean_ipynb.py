#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse
import json

def main():
    """Main function"""

    # PARSE OPTIONS ###########################################################

    # TODO: improve the description
    parser = argparse.ArgumentParser(description='Clean Jupyter Notebook files (.ipynb files).')

    parser.add_argument("fileargs", nargs="+", metavar="FILE", help="Jupyter Notebook files to clean")

    args = parser.parse_args()

    file_paths = args.fileargs

    # CLEAN FILES #############################################################

    output_files = {}

    for file_path in file_paths:
        with open(file_path, 'r') as fd:
            notebook = json.load(fd)

            for cell in notebook['cells']:

                # Init execution_count items
                if "execution_count" in cell:
                    cell["execution_count"] = None

                # Remove outputs
                if "outputs" in cell:
                    cell["outputs"] = []

            output_files[file_path] = notebook

    # SAVE THE RESULT #########################################################

    for file_path, data in output_files.items():
        with open(file_path, 'w') as fd:
            json.dump(data, fd, sort_keys=True, indent=4)  # pretty print format

if __name__ == '__main__':
    main()

