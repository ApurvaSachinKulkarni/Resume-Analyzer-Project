from django.shortcuts import render
from django.core.files.storage import default_storage
import os
from .resume_analyzer import extract_text_from_pdf, extract_skills

def upload_resume(request):
    if request.method == "POST":
        uploaded_file = request.FILES['resume']
        file_path = default_storage.save(uploaded_file.name, uploaded_file)

        raw_skills = request.POST.get('skills', '')
        required_skills = [s.strip().lower() for s in raw_skills.split(',') if s.strip()]

        text = extract_text_from_pdf(file_path)

        detected_skills = extract_skills(text)

        if required_skills:
            matched = list(set(required_skills) & set(detected_skills))
            score = round((len(matched) / len(required_skills)) * 100, 2)
        else:
            matched = detected_skills
            score = round((len(matched) / len(detected_skills)) * 100, 2) if detected_skills else 0

        os.remove(file_path)

        return render(request, 'upload.html', {
            'skills': matched,
            'score': score
        })

    return render(request, 'upload.html')
