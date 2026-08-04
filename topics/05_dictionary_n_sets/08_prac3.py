
# Q: You are given a list of subjects for students, Assume one classroom is required for
# 1 subject. How many classrooms are needed by all students?
# "python", "java", "c++", "python", "javascript", 
# "java", "python", "java", "c++", "c"

# Make Set
subjects = { 
    "python", "java", "c++", "python", "javascript", 
    "java", "python", "java", "c++", "c"
}

print("Number of classrooms needed:", len(subjects))  # Output: Number of classrooms needed: 5, which is the number of unique subjects in the set.

