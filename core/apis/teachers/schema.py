from marshmallow import Schema, fields

class TeacherSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class AssignmentSchema(Schema):
    id = fields.Int()
    student_id = fields.Int()
    teacher_id = fields.Int()
    content = fields.Str()
    grade = fields.Str()
    state = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class AssignmentGradeSchema(Schema):
    id = fields.Int(required=True)
    grade = fields.Str(required=True)
