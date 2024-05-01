##########################
## WARNING              ##
## -------------------- ##
## DO NOT RUN THIS FILE ##
##########################

import os

quine = r"##########################\n## WARNING              ##\n## -------------------- ##\n## DO NOT RUN THIS FILE ##\n##########################\n\nimport os\n\nquine = r\"{quine}\"\nid = {id + 1}\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")"
id = 0

id *= 2
code = f"##########################\n## WARNING              ##\n## -------------------- ##\n## DO NOT RUN THIS FILE ##\n##########################\n\nimport os\n\nquine = r\"{quine}\"\nid = {id + 1}\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")"
open(f"{id + 1}.py", "w").write(code)
os.system(f"python {id + 1}.py")

id += 1
code = f"##########################\n## WARNING              ##\n## -------------------- ##\n## DO NOT RUN THIS FILE ##\n##########################\n\nimport os\n\nquine = r\"{quine}\"\nid = {id + 1}\n\nid *= 2\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")\n\nid += 1\ncode = f\"{quine}\"\nopen(f\"{{id + 1}}.py\", \"w\").write(code)\nos.system(f\"python {{id + 1}}.py\")"
open(f"{id + 1}.py", "w").write(code)
os.system(f"python {id + 1}.py")