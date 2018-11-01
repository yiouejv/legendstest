from config import session as db_session
from apps.front.models import Student, Class, TestPager, Score


stu = db_session.query(Student).filter(Student.student_name=='晓丽').first()
print(stu.student_class)
