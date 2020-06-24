# drf imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# django imports
from datetime import datetime

#app level imports
from .models import User, ActivityPeriod
from .utils import query_debugger

# class UserDataAPIView(APIView):
# 	def get(self, request, format = None):
# 		members = []
# 		user_data = User.objects.all()

# 		# TODO efficiency time complexity(O(n*n))
# 		for user in user_data.iterator():
# 			activities = user.profile.all()
# 			members.append(
# 				{
# 					"id":user.id,
# 					"real_name": user.real_name,
# 					"tz": user.tz,

# 					"activity_periods": [
# 						{"start_time":act.start_time.strftime("%b %d %Y %H:%M %p"),"end_time":act.end_time.strftime("%b %d %Y %H:%M %p")} for act in activities.iterator()

# 					]

# 				}
# 			)
# 		return Response({"ok":True,"members":members,}, status=status.HTTP_200_OK)


# more pythonic  and optimized way 
class UserDataAPIView(APIView):
	""" reduce the time complexity to O(n) and optimized database query"""
	def get(self, request, format = None):
		data_list = []
		data = {}
		qs = User.objects.values_list('id','real_name','tz','profile__start_time','profile__end_time')
		for q in qs.iterator():
			if not bool(data):
				data["id"] = q[0]
				data["real_name"]: q[1]
				data['tz'] = q[2]
				data["activity_periods"] = [ 
					{
						"start_time": q[3].strftime("%b %d %Y %H:%M %p"),
						"end_time": q[4].strftime("%b %d %Y %H:%M %p")
					}
				]

			elif data["id"] == q[0]:
				data['activity_periods'].append(
					{
						"start_time": q[3].strftime("%b %d %Y %H:%M %p"),
						"end_time": q[4].strftime("%b %d %Y %H:%M %p")
					}
				)

			else:
				data_list.append(data)
				data.clear()

		return Response({"members":data_list}, status=status.HTTP_200_OK)
