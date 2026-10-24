
#* =====================
#* RULES FOR FORMATTING
#* =====================
#* 1) Keep spacing and tabs consistent (Tab Size: 2)
#* 2) DO NOT fuck with variables if you don't know what they do
#* 3) If something works, DO NOT FUCKING TOUCH IT
#* 4) Listen to other comments (e.g. labels)
#* 5) Keep names and shit consistent throughout all files
#%important 6) DO NOT FUCKING NEST. NEVER NEST. WE HATE NESTERS. NO STUPID IF STATEMENTS INSIDE OTHER IF STATEMENTS. FIND A BETTER SOLUTION.
#* 7) Try to avoid repeating code. Call another function if you have to
#* 8) Try to keep camelCase and rarely use snake_case
#* 9) If a created function has more than 1 param (or is complex), use a docstring to explain the function

#& ----------------------------------

#* ==========
#* COMMENTING
#* ==========
#%important = Important things to deal with; priorities.
#!bug = Use on the same line as the bug; explain the error.
#todo = Things to do / work on
#note^ = Note for other collaborators. Use on the line below of which it applies to.
#& = Dividers
#~path = Explaining the path of which a file is linked to
#?query = Question or query
#$suggestion = Suggestion for other collaborators
#* = Typically for headings.
#// = Commenting out code