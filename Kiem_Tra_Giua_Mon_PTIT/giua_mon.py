import json

f = open(
    "Kiem_Tra_Giua_Mon_PTIT/data.json",
    "r",
    encoding="utf-8"
)
student_list = json.load(f)
f.close()

while True:

    print(f"""
    {'='*50}
    |               QUẢN LÝ SINH VIÊN                |
    {'='*50}
    |  1. Hiển thị danh sách sinh viên               |
    |  2. Thêm mới sinh viên                         |
    |  3. Cập nhật thông tin sinh viên               |
    |  4. Xóa sinh viên                              |
    |  5. Tìm kiếm sinh viên                         |
    |  6. Sắp xếp danh sách sinh viên                |
    |  7. Thống kê học lực                           |
    |  8. Liệt kê sinh viên điểm cao nhất /thấp nhất |
    |  9. Phân loại học lực                          |
    |  10. Thoát                                     |
    {'='*50}""")
    choice = input("Nhập lựa chọn: ")

    match choice:
        case "1":
            if len(student_list) == 0:
                print("Danh sách hiện đang trống!")

            else:
                print("-" * 80)
                print(f"{'Mã SV':<7} | {'Tên Sinh Viên':<20} | {'Toán':<5} | {'Lý':<5} | {'Hóa':<5} | {'TB':<5} | {'Xếp Loại':^7}")
                print("-" * 80)

                for student in student_list:
                    print(f"{student['id']:<7} | {student['ten']:<20} | {student['diem_toan']:<5} | {student['diem_ly']:<5} | {student['diem_hoa']:<5} | {student['diem_tb']:<5} | {student['xep_loai']:^10}")
                print("-" * 80)

        case "2":

            ma_sv = input("Nhập Mã sinh viên: ").upper().strip()

            check = False

            for student in student_list:

                if student["id"] == ma_sv:
                    check = True
                    break

            if check == True:

                print("MÃ sinh viên đó đã tồn tại!")

            else:
                ten = input("Nhập TÊN sinh viên: ").title().strip()

                diem_toan = float(input("Nhập điểm TOÁN: "))
                diem_ly = float(input("Nhập điểm LÝ: "))
                diem_hoa = float(input("Nhập điểm HÓA: "))

                if diem_toan < 0 or diem_toan > 10:
                    print("Điểm TOÁN nhập KHÔNG hợp lệ!")

                elif diem_ly < 0 or diem_ly > 10:
                    print("Điểm LÝ nhập không hợp lệ!")

                elif diem_hoa < 0 or diem_hoa > 10:
                    print("Điểm HÓA nhập không hợp lệ!")

                else:

                    diem_tb = round((diem_toan + diem_ly + diem_hoa) / 3,2)

                    if diem_tb < 5:
                        xep_loai = "Yếu"

                    elif diem_tb < 7:
                        xep_loai = "Trung Bình"

                    elif diem_tb < 8:
                        xep_loai = "Khá"

                    else:
                        xep_loai = "Giỏi"

                    student = {
                        "id": ma_sv,
                        "ten": ten,
                        "diem_toan": diem_toan,
                        "diem_ly": diem_ly,
                        "diem_hoa": diem_hoa,
                        "diem_tb": diem_tb,
                        "xep_loai": xep_loai
                    }

                    student_list.append(student)

                    f = open("Kiem_Tra_Giua_Mon_PTIT/data.json", "w", encoding="utf-8")
                    json.dump(student_list, f, ensure_ascii=False, indent=4)
                    f.close()

                    print("Thêm thành công!")

        case "3":

            ma_sv = input("Nhập MÃ sinh viên cần sửa: ").upper().strip()

            check = False

            for student in student_list:

                if student["id"] == ma_sv:

                    check = True

                    diem_toan = float(input("Nhập điểm TOÁN mới: "))
                    diem_ly = float(input("Nhập điểm Lý mới: "))
                    diem_hoa = float(input("Nhập điểm Hóa mới: "))

                    if (
                        diem_toan < 0 or diem_toan > 10
                        or diem_ly < 0 or diem_ly > 10
                        or diem_hoa < 0 or diem_hoa > 10
                    ):
                        print("Điểm không hợp lệ!")
                        break

                    student["diem_toan"] = diem_toan
                    student["diem_ly"] = diem_ly
                    student["diem_hoa"] = diem_hoa

                    student["diem_tb"] = round((diem_toan + diem_ly + diem_hoa) / 3,2)

                    if student["diem_tb"] < 5:
                        student["xep_loai"] = "Yếu"

                    elif student["diem_tb"] < 7:
                        student["xep_loai"] = "Trung Bình"

                    elif student["diem_tb"] < 8:
                        student["xep_loai"] = "Khá"

                    else:
                        student["xep_loai"] = "Giỏi"

                    f = open("Kiem_Tra_Giua_Mon_PTIT/data.json", "w", encoding="utf-8")
                    json.dump(student_list, f, ensure_ascii=False, indent=4)
                    f.close()

                    print("Cập nhật thành công!")

                    break

            if check == False:
                print("Không tìm thấy sinh viên bạn vừa nhập!")

        case "4":

            ma_sv = input("Nhập MÃ sinh viên cần xóa: ").upper().strip()

            check = False

            for student in student_list:

                if student["id"] == ma_sv:

                    check = True

                    confirm = input("Bạn có chắc chắn muốn xóa? (y/n): ")

                    if confirm == "y":

                        student_list.remove(student)

                        f = open("Kiem_Tra_Giua_Mon_PTIT/data.json", "w", encoding="utf-8")
                        json.dump(student_list, f, ensure_ascii=False, indent=4)
                        f.close()

                        print(f"Đã xóa thành công {student['ten']}!")

                    break

            if check == False:
                print("Không tìm thấy sinh viên bạn vừa nhập!")

        case "5":

            keyword = input("Nhập MÃ SV hoặc tên cần tìm: ").upper().strip()

            check = False
            
            print("-" * 50)
            print(f"{'Mã SV':<7} | {'Tên':<20} | {'TB':<5} | {'Xếp loại':<10}")

            for student in student_list:
                if (keyword in student["id"].upper() or keyword in student["ten"].upper()):
                    check = True

                    print(
                        f"{student['id']:<7} | "
                        f"{student['ten']:<20} | "
                        f"{student['diem_tb']:<5} | "
                        f"{student['xep_loai']:<10}"
                    )

            if check == False:
                print("Không tìm thấy MÃ SV bạn vừa nhập!")

        case "6":

            print("""
        1. Sap xep theo diem TB giam dan
        2. Sap xep theo ten A-Z""")

            choose = input("Mời bạn nhập lựa chọn: ")

            if choose == "1":

                for i in range(len(student_list) - 1):

                    for j in range(i + 1, len(student_list)):

                        if student_list[i]["diem_tb"] < student_list[j]["diem_tb"]:

                            temp = student_list[i]
                            student_list[i] = student_list[j]
                            student_list[j] = temp

                print("Sắp xếp thành công! Hãy chọn lại chức năng 1 để XEM.")

            elif choose == "2":

                for i in range(len(student_list) - 1):

                    for j in range(i + 1, len(student_list)):

                        if student_list[i]["ten"] > student_list[j]["ten"]:

                            temp = student_list[i]
                            student_list[i] = student_list[j]
                            student_list[j] = temp

                print("Sắp xếp thành công! Hãy chọn lại chức năng 1 để XEM")

        case "7":
            gioi = 0
            kha = 0
            trung_binh = 0
            yeu = 0

            for student in student_list:
                    xep_loai = student["xep_loai"].lower().strip()
                    if xep_loai == "giỏi":
                        gioi += 1
                    elif xep_loai == "khá":
                        kha += 1
                    elif xep_loai == "trung bình":
                        trung_binh += 1
                    else:
                        yeu += 1

            print("-" * 40)
            print(f"{'Xếp loại':<15} | {'Số lượng':^10}")
            print("-" * 40)
            print(f"{'Giỏi':<15} | {gioi:^10}")
            print(f"{'Khá':<15} | {kha:^10}")
            print(f"{'Trung Bình':<15} | {trung_binh:^10}")
            print(f"{'Yếu':<15} | {yeu:^10}")
            print("-" * 40)

        case "8":

            if len(student_list) == 0:

                print("Danh sách trống!")

            else:

                max_student = student_list[0]
                min_student = student_list[0]

                for student in student_list:

                    if student["diem_tb"] > max_student["diem_tb"]:
                        max_student = student

                    if student["diem_tb"] < min_student["diem_tb"]:
                        min_student = student

                print("-" * 80)
                print(f"{'Danh hiệu':<15} | {'Mã SV':<7} | {'Tên Sinh Viên':<20} | {'Điểm TB':<7} | {'Xếp Loại':^10}")
                print("-" * 80)
                print(f"{'Điểm CAO Nhất':<15} | {max_student['id']:<7} | {max_student['ten']:<20} | {max_student['diem_tb']:<7} | {max_student['xep_loai']:^10}")
                print(f"{'Điểm THẤP Nhất':<15} | {min_student['id']:<7} | {min_student['ten']:<20} | {min_student['diem_tb']:<7} | {min_student['xep_loai']:^10}")
                print("-" * 80)

        case "9":
            if len(student_list) == 0:
                print("Danh sách trống!")
            else:
                print("-" * 50)
                print(f"{'Mã SV':<7} | {'Tên Sinh Viên':<22} | {'Xếp Loại':^12}")
                print("-" * 50)

                for student in student_list:
                    print(f"{student['id']:<7} | {student['ten']:<22} | {student['xep_loai']:^12}")
                    
                print("-" * 50)

        case "10":
            print("Cảm ơn bạn đã sử dùng Dịch Vụ! Hệ thống đang đăng xuất...")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ (1-10): ")