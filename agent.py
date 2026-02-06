from core.model import query
import os

# check for workspace dir, where generated code will be written to.
os.makedirs("workspace", exist_ok=True)

# define a goal for the agent

goal = """Task: Create a python script.
        Requirements: 
        Create a list of 10 integers.
        The integers must be hardcoded.
        Compute the sum of the integers.
        Print the code and sum exclusively."""

# assign role

mesg_buff = [{"role": "system", "content": "You are a code generator that can only output valid Python code."}]

# assign task 1 (generate)

mesg_buff.append({"role": "user", "content": goal})
gen_code = query(mesg_buff)
mesg_buff.append({"role": "assistant", "content": gen_code})

# assign task 2 (review)

review_prompt = f"""
Review the code provided for correctness based on:
initial prompt: {goal}.
code: {gen_code}

Output should follow this format:

1) Recieved Code
2) Overall Verdict
3) Issues (if none, say 'no issues')
4) Improvements (2)
"""
mesg_buff.append({"role": "user", "content": review_prompt})
gen_review = query(mesg_buff)

# save generated code to a file

path_code = "workspace/code_0.py"
path_review = "workspace/review_0.py"
with open(path_code, "w") as file_ops:
    file_ops.write(gen_code)
with open(path_review, "w") as file_ops:
    file_ops.write(gen_review)

print(f"Wrote to {path_code} and {path_review}")
