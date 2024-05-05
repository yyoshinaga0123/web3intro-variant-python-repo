class TimesTable:
    @classmethod
    def print_table(cls):
        for i in range(1, 13):
            for j in range(1, 13):
                result = i * j
                print(f"{result:2}", end="\t")
            print()  # Add a newline after each row

# Usage
TimesTable.print_table()