with open("C:\\Users\HP\OneDrive\Documents\Mathematical_related_problem\Mathematical_related_problem\Carols Problems\\input.txt", "r") as f:
    with open("C:\\Users\HP\OneDrive\Documents\Mathematical_related_problem\Mathematical_related_problem\Carols Problems\\input.txt", "w") as f_int:
        line=f.read()
        for line in f:
            tokens=line.split(" ")
            f_int.write(line)
            f_int.read()  #was used to copy the numbers in f, we removed it from the code after doing that so we can be able to only read the file and not write or append.
            print(f_int.read())


        def count_num(num):
            count = 0
            for i in f_int:
                if num == i:
                    count = count + 1
                    continue

            return count

        count = count_num(9)
        print("Number appears:", count, "time(s)")
