# AUTO-GENERATED FILE
# go to https://prairielearn.readthedocs.io/en/latest/python-grader/#serverpy for more info

def generate(data):
    # Define incoming variables here
    names_for_user = [
        # ex: student receives a matrix m
        # {"name": "m", "description": "a 2x2 matrix", "type": "numpy array"}
        { "name": "member", "type": "bool" },
        { "name": "age", "type": "int" },
    ]
    # Define outgoing variables here
    names_from_user = [
        # ex: student defines a determinant function name det
        # {"name": "det", "description": "determinant for a 2x2 matrix", "type": "python function"}
        { "name": "cost", "type": "int" },
    ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user

    return data
