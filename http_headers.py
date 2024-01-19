def write_headers():
    return  "" \
f"""HTTP/1.0 200 OK
"""

def write_blank_line():
    return "" \
"""
"""

def write_404():
    return f"""HTTP/1.0 404 FILE NOT FOUND"""