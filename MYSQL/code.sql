create database patientinformation;

use patientinformation;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE
);

CREATE TABLE medications (
    medication_id INT PRIMARY KEY AUTO_INCREMENT,
    medication_name VARCHAR(100) NOT NULL
);

CREATE TABLE patient_medications (
    patient_medication_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    medication_id INT,
    prescribed_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id)
);


insert into patients(
	patient_id,
    first_name,
    last_name,
    date_of_birth)
values 
(1, 'Hope', 'Test', '1990-04-27'),
(2, 'Ryan', 'Doe', '2000-02-10'),
(3, 'Abbie', 'Gilmore', '2010-11-16'),
(4, 'Nicky', 'Smith', '2020-03-06');

insert into medications(
	medication_id,
    medication_name)
values 
(54, 'zyrtec'),
(10, 'benadryl'),
(20, 'advil'),
(40, 'tylenol');


insert into patient_medications(
	patient_medication_id,
    patient_id,
	medication_id,
    prescribed_date)
values
(5676, 1, 54, '2023-09-06'),
(4637, 2, 10, '2023-10-06'),
(2343, 3, 40, '2023-09-30'),
(8791, 4, 20, '2023-10-10');  



show tables;
select * from patients;
select * from medications;