from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Document
from chroma.db_manager import vecotrdb
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def dashboard(request):
    page_title = "Dashboard"
    context = {"page_title": page_title}

    return render(request, "dashboard.html", context=context)


def filemanager(request):
    page_title = "File Manager"
    context = {}
    if request.method == "GET":
        docs = Document.objects.all()
        context = {"page_title": page_title, "docs": docs}
        return render(request, "filemanager.html", context=context)
    if request.method == "POST":
        try:
            uploaded_file = request.FILES["document"]
            # Document.objects.create(docfile=uploaded_file)

            # DocumentManager(os.path.join(settings.MEDIA_ROOT, "media/documents"))

            # TODO: create upload file to vdb
            messages.success(request, "File uploaded successfully")
        except Exception as e:
            messages.error(request, f"File upload failed: {e}")
            # print(e)
        return redirect("filemanager")


def payroll(request):
    page_title = "Payroll"
    context = {"page_title": page_title}
    return render(request, "payroll.html", context=context)


def performance(request):
    page_title = "Performance"
    context = {"page_title": page_title}
    return render(request, "performance.html", context=context)


def screening(request):
    page_title = "Screening"
    context = {"page_title": page_title}
    return render(request, "screening.html", context=context)


@csrf_exempt
def chatbot(request):
    context = {}
    if request.method == "GET":
        page_title = "Ask Shiru"
        context = {"page_title": page_title}
        return render(request, "chatbot.html", context=context)
    if request.method == "POST":
        query = request.POST["query"]
        qa_chain = vecotrdb.create_qa_chain()
        llm_response = qa_chain(query)
        return JsonResponse(llm_response["result"], safe=False)
