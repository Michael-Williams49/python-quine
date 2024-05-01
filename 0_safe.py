import os

quine = r"import os\n\nquine = r\"{quine}\"\n\nlimit = {limit}\nid = {id + 1}\nif id * 2 >= limit: exit()\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")"

limit = 9
id = 0
if id * 2 >= limit: exit()

id *= 2
code = f"import os\n\nquine = r\"{quine}\"\n\nlimit = {limit}\nid = {id + 1}\nif id * 2 >= limit: exit()\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")"
open(f"{id + 1}.py", "w").write(code)
os.system(f"python {id + 1}.py")

id += 1
code = f"import os\n\nquine = r\"{quine}\"\n\nlimit = {limit}\nid = {id + 1}\nif id * 2 >= limit: exit()\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")"
open(f"{id + 1}.py", "w").write(code)
os.system(f"python {id + 1}.py")
