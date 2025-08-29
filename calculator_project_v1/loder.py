import os

FILE_LOADER = "C:/Users/student.AKTOBE/Desktop/calc"
MAIN_DIR = os.path.join(os.getcwd(), "calculator_project_v1")

def start_downloading():
    if os.path.exists(FILE_LOADER) and os.listdir(FILE_LOADER):
        print("Директория проекта найдена, начинаем установку...")
    else:
        print("Директории не существует или внутри нет файлов.")
        return

    if not os.path.exists(MAIN_DIR):
        os.mkdir(MAIN_DIR)

    for file in os.listdir(FILE_LOADER):
        abs_path_to_file = os.path.join(FILE_LOADER, file)
        if not os.path.isfile(abs_path_to_file):
            print(f"{file} не является файлом, пропускаю")
            continue

        abs_path_to_new_file = os.path.join(MAIN_DIR, file)
        try:
            if os.path.exists(abs_path_to_new_file):
                print(f"Файл {file} существует в папке, удаляю")
                os.remove(abs_path_to_new_file)

            with open(abs_path_to_file, "r", encoding="utf-8") as f:
                with open(abs_path_to_new_file, "w", encoding="utf-8") as f2:
                    f2.write(f.read())
        except Exception as e:
            print(f"Ошибка при копировании {file}: {e}")

if __name__ == "__main__":
    start_downloading()



