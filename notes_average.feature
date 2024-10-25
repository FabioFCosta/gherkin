Feature: Student Notes Average
    Scenario Outline: Calculate student average and situation
        Given the student <student_login>
        And the discipline <discipline_cod>
        And discipline schedule with <ds> hours
        When the user informs the avaliation 1 note equals to <av1_note>
        And the avaliation 2 note equals to <av2_note>
        And the student has <absents> classes absents
        Then the system calculates the student's average
        And determines the student situation: <expected_situation>

        Examples:
            | student_login | discipline_cod | ds | av1_note | av2_note | absents | expected_situation     |
            | fabio.costa   | DFMEA-0001     | 64 | 5        | 4        | 0       | repproved by note      |
            | fabio.costa   | DFMEA-0001     | 64 | 10       | 9        | 17      | repproved by frequency |
            | fabio.freitas | DFMEA-0001     | 64 | 8        | 0        | 11      | repproved by note      |
            | fabio.freitas | DFMEA-0001     | 64 | 9        | 10       | 12      | approved               |