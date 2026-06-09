from sqlalchemy import create_engine,inspect, text
from SubjectTable import SubjectTable

db = SubjectTable("postgresql://postgres:123@localhost:5432/Lesson3")


def test_get_subject():
    result = db.get_subjects()
    assert len(result) > 0

def test_add_subject():
    result1 = db.get_subjects()
    name= "Зельеварение"
    db.create_subject(name)
    result2 = db.get_subjects()
    assert result2[-1]['subject_title'] == name
    assert len(result1)<len(result2)

def test_update_subject():
    db.update_subject(9,'Зельеварение')
    result = db.get_subjects()
    assert result[-1]['subject_id']==9
def test_delete_subject():
   res1 = db.get_subjects()
   db.delete_subject('Зельеварение')
   res2=db.get_subjects()
   assert len(res1)>len(res2)


# def test_add_subject():
#     connection = db.connect()
#     transaction = connection.begin()
#     result1= connection.execute(text("SELECT *FROM subject"))
#     list_before = result1.mappings().all()
#     sql = text('INSERT INTO subject(\"subject_title\") VALUES(:new_subject)')
#     connection.execute(sql,{'new_subject': 'Новый предмет'})
#     result2 = connection.execute(text("SELECT *FROM subject"))
#     list_after = result2.mappings().all()
#     assert len(list_after) - len(list_before) == 1
#     transaction.commit()
#     connection.close()
# def test_update_subject():
#     connection = db.connect()
#     transaction = connection.begin()
#     sql=text("UPDATE subject SET subject_id =:new_id WHERE subject_title ='Новый предмет'")
#     connection.execute(sql,{'new_id': '9'})
#     result = (connection.execute(text("SELECT *FROM subject"))).mappings().all()
#     last_row= result[-1]
#     transaction.commit()
#     connection.close()
#     assert last_row['subject_id'] == 9
# def test_delete_subject():
#     connection = db.connect()
#     transaction = connection.begin()
#     result1 = connection.execute(text("SELECT *FROM subject"))
#     list_before = result1.mappings().all()
#     sql = text("DELETE FROM subject WHERE subject_title =:subject_to_delete")
#     connection.execute(sql,{'subject_to_delete':'Новый предмет'})
#     result2 = connection.execute(text("SELECT *FROM subject"))
#     list_after = result2.mappings().all()
#     transaction.commit()
#     connection.close()
#     assert len(list_before) - len(list_after) == 1