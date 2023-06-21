def main():
    total_males = input("Write the number of male students: ")
    total_females = input("Write the number of female students: ")

    total_students = int(total_males) + int(total_females)
    m_perc:float
    f_perc:float
    m_perc = (int(total_males) / total_students) * 100
    f_perc = (int(total_females) / total_students) * 100

    print("The total number of students: "f"{total_students}")
    print("The number of males and females: "f'{total_males} \t {total_females}')
    print("The percentage of males and females: "f'{m_perc:.2f} % \t {f_perc:.2f} %')
    
    return m_perc, f_perc
if __name__ == '__main__':
    main()
