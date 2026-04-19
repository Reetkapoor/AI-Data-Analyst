from core.llm_sql import is_data_question

question = "how are you"

if("YES" in is_data_question(question)):
    print("yes")
else:
    print("no")

