from FIApp1.models import User


def courselist(user_id):
    classes = list(User.objects.aggregate(*[
                {
                    '$lookup': {
                        'from': 'enrolment',
                        'localField': 'user_id',
                        'foreignField': 'user_id',
                        'as': 'r1'
                    }
                }, {
                    '$unwind': {
                        'path': '$r1',
                        'includeArrayIndex': 'r1_id',
                        'preserveNullAndEmptyArrays': False
                    }
                }, {
                    '$lookup': {
                        'from': 'course',
                        'localField': 'r1.courseID',
                        'foreignField': 'courseID',
                        'as': 'r2'
                    }
                }, {
                    '$unwind': {
                        'path': '$r2',
                        'preserveNullAndEmptyArrays': False
                    }
                }, {
                    '$match': {
                        'user_id': user_id
                    }
                }, {
                    '$sort': {
                        'courseID': 1
                    }
                }
            ]))
    return classes
