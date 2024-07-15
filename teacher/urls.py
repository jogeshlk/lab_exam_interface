from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-add-code-exam',views.teacher_add_code_exam_view,name='teacher-add-code_exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('teacher-view-code-exam', views.teacher_view_code_exam_view,name='teacher-view-code-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),
path('delete-code-exam/<int:pk>', views.delete_code_exam_view,name='delete-code-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-add-code-question', views.teacher_add_code_question_view,name='teacher-add-code-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('teacher-view-code-question', views.teacher_view_code_question_view,name='teacher-view-code-question'),

path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('see-code-question/<int:pk>', views.see_code_question_view,name='see-code-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
path('remove-code-question/<int:pk>', views.remove_code_question_view,name='remove-code-question'),
]