def save_as_csv(file_name, lines, fields):
    """Сохраняет файл в виде csv файла 

        Args:
            file_name (str): Название файла
            fields (str): Поля csv файла
            lines (str): Вакансии через \n
    """
    print("Saving", file_name)
    with open("csv/vacancies_"+file_name+".csv", 'w', encoding="utf-8-sig") as f_out:
        f_out.write(fields)
        f_out.writelines(lines)
        f_out.close()

def сsv_chuncker(file_name):
    """Разделяет вакансии по годам и сохраняет их

        Args:
            file_name (str): Название файла для разделения
    """
    csvs = {}
    with open(ﬁle_name, encoding="UTF-8-sig") as File:
        fields = File.readline()
        for row in File:
            year = row.split(",")[len(row.split(",")) - 1][0:4]
            if year not in csvs:
                csvs[year] = []
            csvs[year].append(row)
    for vacancy in csvs:
        if len(csvs) > 0:
            save_as_csv(vacancy, csvs[vacancy], fields)

file_name = input("Введите название файла: ")
сsv_chuncker(file_name)