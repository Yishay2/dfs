from number_of_islands import count_islands  # הנחה שהפונקציה ממוקמת בקובץ נפרד


def test_count_islands():
    # מקרה בסיסי עם כמה איים
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert count_islands(grid1) == 3

    # רשת ריקה
    grid2 = []
    assert count_islands(grid2) == 0

    # רשת של מים בלבד
    grid3 = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert count_islands(grid3) == 0

    # רשת של אדמה בלבד
    grid4 = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    assert count_islands(grid4) == 1

    # אי בודד
    grid5 = [["1"]]
    assert count_islands(grid5) == 1

    # מים בלבד, תא בודד
    grid6 = [["0"]]
    assert count_islands(grid6) == 0

    # כמה איים קטנים
    grid7 = [
        ["1", "0", "0", "1"],
        ["0", "0", "1", "0"],
        ["1", "0", "0", "1"]
    ]
    assert count_islands(grid7) == 5

    # רשת מלבנית עם אי גדול אחד ואיים קטנים
    grid8 = [
        ["1", "1", "0", "0", "0", "1"],
        ["1", "1", "0", "1", "1", "1"],
        ["0", "0", "0", "1", "0", "0"],
        ["1", "0", "0", "1", "1", "0"],
        ["1", "1", "0", "0", "0", "0"]
    ]
    assert count_islands(grid8) == 3

    # רשת עם אדמות המחוברות באלכסון (לא מחוברות אנכית/אופקית)
    grid9 = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"]
    ]
    assert count_islands(grid9) == 5  # אלכסון לא נחשב חיבור

    # רשת מלבנית עם אפס שורות
    grid10 = [[]]
    assert count_islands(grid10) == 0

    # רשת גדולה (מקרה גבול)
    grid11 = [
        ["1" if (i + j) % 2 == 0 else "0" for j in range(300)]
        for i in range(300)
    ]
    assert count_islands(grid11) == 45000  # כל תא '1' הוא אי נפרד

    print("All test cases passed!")


# הפעלת הטסטים
test_count_islands()
