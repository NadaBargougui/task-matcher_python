from django.shortcuts import render
from .forms import TaskForm
from .matcher import get_unassigned_employees, extract_task_skills, match_task_to_employee

def match_view(request):
    best_match = None
    match_score = None
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            task_skills = extract_task_skills(desc)
            employees = get_unassigned_employees('./resumes')
            matches = match_task_to_employee(task_skills, employees)

            if matches:
                best_match, raw_score = matches[0]
                match_score = round(raw_score * 100)
            else:
                best_match = "No match found"
    else:
        form = TaskForm()

    return render(request, 'match.html', {
        'form': form,
        'best_match': best_match,
        'match_score': match_score
    })
