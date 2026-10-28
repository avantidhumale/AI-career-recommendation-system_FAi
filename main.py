import tkinter as tk
from tkinter import ttk, messagebox

# AI Career Recommendation System
# Rule-based prototype: matches selected interests and skills with career profiles.

CAREERS = [
    {
        "name": "AI / Machine Learning Engineer",
        "interests": {"Artificial Intelligence", "Problem Solving", "Mathematics"},
        "skills": {"Python", "Mathematics", "Data Analysis"},
        "roadmap": "Learn Python, statistics, machine learning basics, and build AI projects."
    },
    {
        "name": "Data Analyst",
        "interests": {"Data Analysis", "Problem Solving", "Business"},
        "skills": {"Python", "Data Analysis", "SQL"},
        "roadmap": "Learn Excel, SQL, Python, data visualization, and dashboard tools."
    },
    {
        "name": "Web Developer",
        "interests": {"Web Development", "Design", "Problem Solving"},
        "skills": {"HTML/CSS", "JavaScript", "Python"},
        "roadmap": "Learn HTML, CSS, JavaScript, responsive design, and Git/GitHub."
    },
    {
        "name": "Cybersecurity Analyst",
        "interests": {"Cybersecurity", "Problem Solving", "Networking"},
        "skills": {"Networking", "Python", "Linux"},
        "roadmap": "Learn networking, Linux, security fundamentals, and safe lab practice."
    },
    {
        "name": "Software Developer",
        "interests": {"Software Development", "Problem Solving", "Design"},
        "skills": {"Python", "JavaScript", "SQL"},
        "roadmap": "Practice programming, data structures, databases, testing, and Git."
    },
    {
        "name": "Cloud Engineer",
        "interests": {"Cloud Computing", "Networking", "Software Development"},
        "skills": {"Networking", "Linux", "Python"},
        "roadmap": "Learn Linux, networking, cloud concepts, containers, and deployment."
    }
]

INTERESTS = [
    "Artificial Intelligence", "Data Analysis", "Web Development",
    "Cybersecurity", "Software Development", "Cloud Computing",
    "Problem Solving", "Mathematics", "Design", "Business", "Networking"
]
SKILLS = [
    "Python", "Mathematics", "Data Analysis", "SQL", "HTML/CSS",
    "JavaScript", "Networking", "Linux"
]

def recommend():
    selected_interests = {item for item, var in interest_vars.items() if var.get()}
    selected_skills = {item for item, var in skill_vars.items() if var.get()}

    if not selected_interests and not selected_skills:
        messagebox.showwarning("Select options", "Please select at least one interest or skill.")
        return

    results = []
    for career in CAREERS:
        interest_matches = len(selected_interests & career["interests"])
        skill_matches = len(selected_skills & career["skills"])
        score = interest_matches + skill_matches
        if score:
            results.append((score, career, interest_matches, skill_matches))

    results.sort(key=lambda item: item[0], reverse=True)
    output.configure(state="normal")
    output.delete("1.0", tk.END)

    if not results:
        output.insert(tk.END, "No close match found. Try selecting different interests or skills.")
    else:
        for score, career, interest_count, skill_count in results:
            output.insert(tk.END, f'{career["name"]}  | Match score: {score}\\n')
            output.insert(tk.END, f'  Matching interests: {interest_count} | Matching skills: {skill_count}\\n')
            output.insert(tk.END, f'  Learning roadmap: {career["roadmap"]}\\n')
            output.insert(tk.END, "-" * 68 + "\\n")
    output.configure(state="disabled")

def clear_all():
    for var in interest_vars.values():
        var.set(False)
    for var in skill_vars.values():
        var.set(False)
    output.configure(state="normal")
    output.delete("1.0", tk.END)
    output.configure(state="disabled")

root = tk.Tk()
root.title("AI Career Recommendation System")
root.geometry("900x720")
root.minsize(760, 620)
root.configure(bg="#f2f5fb")

style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass
style.configure("TLabel", background="#f2f5fb", font=("Segoe UI", 10))
style.configure("Title.TLabel", background="#f2f5fb", foreground="#173b70",
                font=("Segoe UI", 20, "bold"))
style.configure("Section.TLabel", background="#f2f5fb", foreground="#173b70",
                font=("Segoe UI", 12, "bold"))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)

title = ttk.Label(root, text="AI Career Recommendation System", style="Title.TLabel")
title.pack(pady=(16, 4))
subtitle = ttk.Label(root, text="Choose your interests and skills to explore matching careers.")
subtitle.pack(pady=(0, 12))

main = ttk.Frame(root, padding=12)
main.pack(fill="both", expand=True, padx=16, pady=4)
main.configure(style="TFrame")
style.configure("TFrame", background="#f2f5fb")

left = ttk.Frame(main, padding=10)
left.pack(side="left", fill="y", padx=(0, 12))

right = ttk.Frame(main, padding=10)
right.pack(side="left", fill="both", expand=True)

ttk.Label(left, text="Your Interests", style="Section.TLabel").pack(anchor="w", pady=(0, 6))
interest_vars = {}
for item in INTERESTS:
    var = tk.BooleanVar(value=False)
    interest_vars[item] = var
    ttk.Checkbutton(left, text=item, variable=var).pack(anchor="w", pady=2)

ttk.Label(left, text="Your Skills", style="Section.TLabel").pack(anchor="w", pady=(14, 6))
skill_vars = {}
for item in SKILLS:
    var = tk.BooleanVar(value=False)
    skill_vars[item] = var
    ttk.Checkbutton(left, text=item, variable=var).pack(anchor="w", pady=2)

buttons = ttk.Frame(left)
buttons.pack(fill="x", pady=16)
ttk.Button(buttons, text="Recommend Careers", command=recommend).pack(fill="x", pady=4)
ttk.Button(buttons, text="Clear Selections", command=clear_all).pack(fill="x", pady=4)

ttk.Label(right, text="Recommended Careers & Learning Roadmaps",
          style="Section.TLabel").pack(anchor="w", pady=(0, 8))
output = tk.Text(right, wrap="word", font=("Consolas", 10), bg="white",
                 fg="#202b3c", relief="flat", padx=12, pady=12)
output.pack(fill="both", expand=True)
output.configure(state="disabled")

footer = ttk.Label(root, text="Note: This is a basic rule-based prototype, not a trained machine-learning model.")
footer.pack(pady=(0, 12))

root.mainloop()
