"""
Module to inline python code.
"""

import re

with open("autres/inline_exapmle.py", "r", encoding="utf-8") as file_input, open(
    "autres/inline_example_inlined.py", "w", encoding="utf-8"
) as file_output:
    lines = file_input.readlines()
    file_output.write("(lambda:(")
    output_end = "))()"
    match_comments = re.compile(r"#.*")
    match_assignation = re.compile(r"[^=]+=[^=]+")
    var = True
    for line in lines:
        line = line.strip()
        if match_comments.match(line) or line == "":
            continue
        match_comments.sub("", line)
        if match_assignation.match(line):
            var_name = line.split("=")[0].strip()
            var_value = line.split("=")[1].strip()
            file_output.write(f"(lambda {var_name}:(")
            output_end = f"))({var_value})" + output_end
            continue
        if line[-1] == ":":
            match line.split(" ")[0]:
                case "if":
                    file_output.truncate()
                    file_output.write("(lambda:(")
                    output_end = line[:-1] + " else ()))()" + output_end
                case "for":
                    file_output.write("(lambda:((")
                    output_end = ")" + line[:-1] + ")))()" + output_end
            var = True
        else:
            if not var:
                file_output.write(",")
            file_output.write(line.strip())
            var = False
    file_output.write(output_end)
