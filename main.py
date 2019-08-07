import project1
import project2
import project3
import project4


def main():
    project_id = 2
    if project_id == 1:
        project1.execute()
    elif project_id == 2:
        project2.execute()
    elif project_id == 3:
        project3.execute()
    elif project_id == 4:
        project4.execute()


if __name__ == "__main__":
    main()