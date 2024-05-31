todos = [
    {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False,
    },
    {"userId": 1, "id": 1, "title": "fugiat veniam minus", "completed": False},
    {"userId": 1, "id": 4, "title": "et porro tempora", "completed": True},
    {
        "userId": 1,
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
        "completed": False,
    },
]
done_task = 0
undone_task = 0
for todo in todos:
	if todo['id'] == 1:
		if todo["completed"] == False:
			undone_task += 1
		elif todo["completed"] == True:
			done_task += 1
print(undone_task)
