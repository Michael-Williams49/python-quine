quine = r"quine = r\"{quine}\"\ncode = f\"{quine}\"\nopen(\"quine.py\", \"w\").write(code)"
code = f"quine = r\"{quine}\"\ncode = f\"{quine}\"\nopen(\"quine.py\", \"w\").write(code)"
open("quine.py", "w").write(code)