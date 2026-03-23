-- Attendance Project In Universitie
-- =================================

create database ATTENDANCE;
use ATTENDANCE;
create table University(
UnID varchar(8) not null,
Name Varchar(50) not null,
primary key(UnID));

create table Employees(
EmployeeID varchar(10) not null,
Title varchar(5),
First_Name varchar(30),
Last_Name varchar(30),
Interested varchar(200),
UniversityID varchar(8) not null,
primary key(EmployeeID),
foreign key(UniversityID) references University(UnID));


create table campus(
CampsID varchar(8) not null,
Name varchar(100) not null,
location varchar(50),
UniversityID varchar(8) not null,
HeadID varchar(10),
primary key (CampsID),
foreign key (UniversityID) references University(UnID),
foreign key (HeadID) references Employees(EmployeeID));

create table School(
SchoolID varchar(8) not null,
Name varchar(150) not null,
CampusID varchar(8),
primary key(SchoolID),
foreign key (CampusID) references campus(CampsID));

create table Department(
DeptID varchar(10) not null,
Name varchar(100) not null,
SchoolID varchar(10) not null,
primary key (DeptID),
foreign key (SchoolID) references School(SchoolID));

create table Course(
CourseID varchar(10) not null,
CourseName varchar(100),
credit int(4),
DeptID varchar(10) not null,
primary key(CourseID),
foreign key (DeptID) references Department(DeptID));


create table Lecturer(
LecturerID varchar(10) not null,
Title varchar(5),
First_name varchar(30),
Last_name varchar(30),
CourseID varchar(10) not null,
primary key (LecturerID),
foreign key (CourseID) references Course(CourseID));

create table teaching_to(
startdate date,
lectureID varchar(10) not null,
Department varchar(10) not null,
primary key(lectureID, Department),
foreign key(LectureID) references Lecturer(LecturerID),
foreign key(Department) references Department(DeptID));


CREATE TABLE Timetable (
    TimetableID INT AUTO_INCREMENT PRIMARY KEY,
    CourseID varchar(10) NOT NULL,
    CampusID varchar(10) NOT NULL,
    Room VARCHAR(50),
    DayOfWeek ENUM('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    SemesterID INT NOT NULL,
    accademic_year varchar(20),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
	FOREIGN KEY (CampusID) REFERENCES campus(CampsID)
);
CREATE TABLE ClassSession (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,
    TimetableID INT NOT NULL,
    SessionDate DATE NOT NULL,
    AttendanceCode VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status ENUM('Open','Closed') DEFAULT 'Open',
	FOREIGN KEY (TimetableID) REFERENCES Timetable(TimetableID)
);
create table Student(
Reg_number varchar(10) not null,
First_name varchar(30),
last_name varchar(30),
primary key(Reg_number),
departmentID varchar(10),
foreign key (departmentID) references Department(DeptID));

create table enrollement(
startime date,
Reg_number varchar(10) not null ,
CourseID varchar(10) not null,
primary key(Reg_number, courseID),
foreign key (Reg_number)  references Student(Reg_number),
foreign key(CourseID) references Course(CourseID));

CREATE TABLE Attendance (
    AttendanceID BIGINT AUTO_INCREMENT PRIMARY KEY,
    SessionID INT NOT NULL,
    Reg_number varchar(10) NOT NULL,
    Status ENUM('Present','Absent','Late') DEFAULT 'Absent',
    TimeRecorded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (SessionID) REFERENCES ClassSession(SessionID),
	FOREIGN KEY (Reg_number) REFERENCES Student(Reg_number),

    CONSTRAINT unique_attendance
        UNIQUE (SessionID, Reg_number)
);

show tables;
ALTER TABLE University
ADD Head VARCHAR(10),
ADD FOREIGN KEY (Head) REFERENCES Employees(EmployeeID)
;

alter table Department
add HeadofDeparment varchar(10),
add foreign key(HeadofDeparment) references Lecturer(LecturerID);

create table Course_Progrees(
    CourseId varchar(10) not null,
    DepartmentID varchar(10) not null,
    LecturerID varchar(10) not null,
    week int(1),
    Date date,
    startime datetime,
    endtime datetime,
    topic varchar(255),
    Level int(2),
    primary key(CourseId, DepartmentID, Level,LecturerID),
    foreign key (CourseId) references Course(CourseID),
    foreign key (DepartmentID) references Department(DeptID),
    foreign key (LecturerID) references Lecturer(LecturerID)
);



