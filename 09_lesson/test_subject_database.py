from SubjectTable import SubjectTable

db = SubjectTable("postgresql://postgres:123@localhost:5432/Lesson3")


def test_get_subject():
    result = db.get_subjects()
    assert len(result) > 0

def test_add_subject():
    result1 = db.get_subjects()
    name = "Зельеварение"
    new_id = 15
    db.create_subject(new_id, name)
    result2 = db.get_subjects()
    assert result2[-1]['subject_title'] == name
    assert len(result1)<len(result2)

def test_update_subject():
    name = 'Защита от злых чар'
    new_id = 12412
    db.create_subject(new_id, name)
    db.update_subject(213, name)
    result = db.get_subjects()
    assert result[-1]['subject_id'] != new_id

def test_delete_subject():
    name="Предмет на  удаление"
    new_id= 124
    db.create_subject(new_id, name)
    res1 = db.get_subjects()
    db.delete_subject(name)
    res2=db.get_subjects()
    assert len(res1)>len(res2)

