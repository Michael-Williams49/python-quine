import os

quine = r"quine = r\"{quine}\"\nid = {id + 1}\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)"
id = 0

id *= 2
code = f"quine = r\"{quine}\"\nid = {id + 1}\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)"
open(f"{id + 1}.py", "w").write(code)
os.system(f"python {id + 1}.py")

id += 1
code = f"quine = r\"{quine}\"\nid = {id + 1}\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)"
open(f"{id + 1}.py", "w").write(code)
os.system(f"python {id + 1}.py")