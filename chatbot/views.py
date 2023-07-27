from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'HI THIS IS MY RESPONSE'
        return JsonResponse({'message':message,'response': response})
    return render(request, 'chatbot.html')