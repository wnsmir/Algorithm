-- 학과 테이블
CREATE TABLE Department (
    DepartmentCode VARCHAR(10) PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    BuildingRoom VARCHAR(50),
    OfficePhone VARCHAR(15),
    CollegeName VARCHAR(100)
);

-- 교수 테이블
CREATE TABLE Professor (
    ProfessorID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    SSN VARCHAR(15),
    Address VARCHAR(200),
    Phone VARCHAR(15),
    DepartmentCode VARCHAR(10),
    FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode)
);

-- 학생 테이블
CREATE TABLE Student (
    StudentID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    SSN VARCHAR(15),
    Address VARCHAR(200),
    Phone VARCHAR(15),
    Birthdate DATE,
    Gender CHAR(1),
    Year INT,
    DepartmentCode VARCHAR(10),
    FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode)
);

-- 과목 테이블
CREATE TABLE Course (
    CourseCode VARCHAR(10) PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    Credits INT,
    DepartmentCode VARCHAR(10),
    FOREIGN KEY (DepartmentCode) REFERENCES Department(DepartmentCode)
);

-- 분반 테이블
CREATE TABLE Class (
    CourseCode VARCHAR(10),
    ClassNumber INT,
    ProfessorID VARCHAR(10),
    YearSemester VARCHAR(10),
    Classroom VARCHAR(50),
    PRIMARY KEY (CourseCode, ClassNumber),
    FOREIGN KEY (CourseCode) REFERENCES Course(CourseCode),
    FOREIGN KEY (ProfessorID) REFERENCES Professor(ProfessorID)
);

-- 지도 테이블
CREATE TABLE Guidance (
    StudentID VARCHAR(10),
    ProfessorID VARCHAR(10),
    GuidanceStartDate DATE,
    GuidanceEndDate DATE,
    PRIMARY KEY (StudentID, ProfessorID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ProfessorID) REFERENCES Professor(ProfessorID)
);