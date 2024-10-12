from django.db import models
from teams.models import Team
from problems.models import Problem

class Submission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Submission by {self.team} for {self.problem}'
