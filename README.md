# IncludeMD

a preprocessor that simply includes other files, even recursively!

usage in markdown:

    :::markdown
    ...
    #include filename
    ...


usage in python:

    :::python
    from includemd import IncludeMD

    ...
    markdown.markdown(text, extensions=[
        ...
        IncludeMD(path=os.path.dirname(infile)),
        ...
    ])
    ...

## Installation

    :::bash
    pip install git+https://github.com/maxdoom-com/includemd.git
