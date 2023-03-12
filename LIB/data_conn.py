import sqlite3


class Database():
    def __init__(self, DB):
        self.db = DB
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

    def getAll(self, table):
        self.cursor.execute(f"select * from {table}")
        results = self.cursor.fetchall()
        return results

    def getData(self, table, attr, criteria):
        self.cursorObj.execute(f"SELECT * FROM {table} WHERE {attr} like ?", ("%" + criteria + "%",))
        results = self.cursorObj.fetchall()
        return results

    def get_fields(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        Fields = [field[0] for field in self.cursor.description]
        return Fields

    def getQuestions(self):
        self.cursor.execute(f"select question, answer from questions")
        questions = self.cursor.fetchall()
        return questions

    def getQuestionAnswer(self, testID):
        self.cursor.execute(f"SELECT QUESTIONS.QuestionID, QUESTIONS.Question, QUESTIONS.Answer FROM QUESTIONS \
                            INNER JOIN TEST_PARTS ON QUESTIONS.QuestionID = TEST_PARTS.QuestionID WHERE (((TEST_PARTS.TESTID)={testID}))")
        q_answer = self.cursor.fetchall()
        return q_answer

    def removeQuestion(self, id):
        self.cursor.execute(f"delete from test_parts where questionID = {id}")
        self.connection.commit()

    def getNewQuestions(self, topic):
        self.cursor.execute(f"select questionID, question, answer from questions where topic = '{topic}'")
        questions = self.cursor.fetchall()
        return questions

    def addData(self, table, values):
        count = len(values)
        self.cursor.execute(f"insert into {table} values ("+",".join(count * "?")+")",(values))
        self.connection.commit()

    def generalSQL(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def addRecord(self, table, values):
        count = len(values)
        self.cursor.execute(f"insert into {table} values (null,"+",".join(count * "?")+")",(values))
        self.connection.commit()

    def deleteRecord(self, attr, table, criteria):
        self.cursor.execute(f"delete from {table} where \"{attr}\" = ?",(criteria,))
        self.connection.commit()

    def getStudentGrades(self, id):
        self.cursor.execute(f"SELECT STUDENT.StudentID, TEST.TestName, \
        TEST.Topic, TEST.Difficulty, SITS.Date_Sat, SITS.Score FROM TEST \
        INNER JOIN (STUDENT INNER JOIN SITS ON STUDENT.StudentID = SITS.StudentID) \
        ON TEST.TestID = SITS.TestID where STUDENT.StudentID ={id};")
        grades = self.cursor.fetchall()
        return grades

    def getAllScores(self):
        self.cursor.execute("SELECT STUDENT.Forename, STUDENT.Surname, STUDENT.TutorGrp, Sum(SITS.Score) AS SumOfScore\
        FROM TEST INNER JOIN (STUDENT INNER JOIN SITS ON STUDENT.StudentID = SITS.StudentID) ON TEST.TestID = SITS.TestID\
        GROUP BY STUDENT.Forename, STUDENT.Surname, STUDENT.TutorGrp\
        ORDER BY Sum(SITS.Score) DESC;")
        results = self.cursor.fetchall()
        return results

if __name__ == "__main__":
    pass

