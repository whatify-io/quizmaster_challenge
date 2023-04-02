from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["GET"])
def quiz_list(request):
    ## TODO: Implement logic to get all quizzes
    return JsonResponse({"quizzes": []}, safe=False)

@api_view(["GET"])
def quiz_detail(request, quiz_id):
    ## TODO: Implement logic to get a quiz by its id
    return JsonResponse({})

@api_view(["POST"])
def create_new_quiz(request):
    quiz_data = request.data
    ## TODO: Implement logic to create a new quiz with data passed in POST request body
    return JsonResponse({})

@api_view(["POST"])
def submit_quiz(request, quiz_id):
    # TODO: Implement the logic for quiz submission and scoring
    pass
