from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime


from .models import User, ActivityPeriod

class UserDataAPIView(APIView):
	def get(self, request, format = None):
		members = []
		user_data = User.objects.all()

		# TODO efficiency time complexity(O(n*n))
		for user in user_data.iterator():
			activities = user.profile.all()
			members.append(
				{
					"id":user.id,
					"real_name": user.real_name,
					"tz": user.tz,

					"activity_periods": [
						{"start_time":act.start_time.strftime("%b %d %Y %H:%M %p"),"end_time":act.end_time.strftime("%b %d %Y %H:%M %p")} for act in activities.iterator()

					]

				}
			)
		return Response({"ok":True,"members":members,}, status=status.HTTP_200_OK)


