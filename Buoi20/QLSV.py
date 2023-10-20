class Student:
    def __init__(self, masv, ho_ten, ngay_sinh, que_quan, chuyen_nganh, lop):
        self.masv = masv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.que_quan = que_quan
        self.chuyen_nganh = chuyen_nganh
        self.lop = lop

    def __str__(self):
        return f"{self.masv:5}  {self.ho_ten:20}  {self.ngay_sinh}  {self.que_quan:15}  {self.chuyen_nganh:10}  {self.lop}"


class Student_List:
    def __init__(self, student_list = []):
        self.student_list = student_list

    def display(self):
        # Xem danh mục sinh viên
        for student in self.student_list:
            print(student)

    def add_student(self, student):
        # Thêm sinh viên vào danh mục
        self.student_list.append(student)

    def search(self, keyword):
        results = list(filter(lambda student: student.masv == keyword, self.student_list))
        # print(results[0] if len(results) > 0 else 'Not found')
        return results[0] if len(results) > 0 else None

    def update_student(self, student):
        # Cập nhật sinh viên vào danh mục
        pass

    def delete_student(self, keyword):
        found_student = self.search(keyword)
        if found_student:
            self.student_list.remove(found_student)
            print("Sau khi xóa:")
            self.display()
        else:
            print("Tìm không thấy SV có mã để xóa")

    def sort(self):
        pass


# Demo
sv1 = Student(101, 'Tèo', '2000-10-20', 'Hà Nội', 'CNPM', 'CNPM.K23')
sv2 = Student(102, 'Tý', '2000-12-12', 'Hồ Chí Minh', 'CNPM', 'CNPM.K23')
# print(sv1) #???

sl = Student_List([sv2])
sl.add_student(sv1)
sl.display()

sl.search(104)

sl.delete_student(101)
