
#!/usr/bin/python3
""" Module holds pascal triangle function """


def pascal_triangle(n):
    """ pascal triangle """
    pascal_list = []
    for _ in range(n):
        row = [1]
        if pascal_list:
            last_row = pascal_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_list.append(row)
    return pascal_list
