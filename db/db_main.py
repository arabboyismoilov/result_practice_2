import mysql.connector

DB_NAME = 'result_practice4'

# ushbularni o'ziznikiga o'zgartiring
DB_HOST = 'localhost'
DB_USER = 'admin'
DB_PASSWORD = 'admin'

def init_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        create_db_script = f"""
            create database IF NOT EXISTS {DB_NAME};
        """

        use_db_script = f"""use {DB_NAME};"""

        create_student_table_script = """create table IF NOT EXISTS student(
            id bigint auto_increment primary key,
            username varchar(50) not null unique,
            password varchar(50) not null,
            created_date timestamp default CURRENT_TIMESTAMP
        );
        """

        create_courses_table_script = """
            create table IF NOT EXISTS courses(
                id bigint auto_increment primary key,
                nomi varchar(50) not null,
                narxi decimal(10, 2) not null,
                davomiyligi varchar(50),
                created_date timestamp default CURRENT_TIMESTAMP
            );
        """

        create_student_courses_table_script = """
            create table IF NOT EXISTS student_courses(
                id bigint auto_increment primary key,
                student_id bigint,
                course_id bigint,
                foreign key(student_id) REFERENCES student(id),
                foreign key(course_id) REFERENCES courses(id)
            );
        """

        insert_students_script = """
            insert ignore into student(username, password) values("admin", "admin");
        """

        cur = conn.cursor()

        cur.execute(create_db_script)
        conn.commit()

        cur.execute(use_db_script)
        conn.commit()

        cur.execute(create_courses_table_script)
        conn.commit()

        cur.execute(create_student_table_script)
        conn.commit()

        cur.execute(create_student_courses_table_script)
        conn.commit()

        cur.execute(insert_students_script)
        conn.commit()

        conn.commit()

        cur.close()
        conn.close()

    except mysql.connector.Error as e:
        print(e)
