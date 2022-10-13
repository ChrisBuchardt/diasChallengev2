# DIASCodingChallenge
DIAS REST Api challenge written in Java

Challenge One Patient
------------------------------------------------------------------------
A hospital needs a new medical journal system to manage doctor-patient relations. They would like to prohibit doctors in one department from access the medical journal of a patient admitted to another department.

Create a REST web service in a language of your choice. We prefer Node.js, Python, Java or Go using a framework. The service should be runnable with Docker.


The API should have three concepts: admission, medical journal(patient) and doctor. ​
An admission has at least the following attributes:
	Department
	Zero or more doctors
	One medical journal

A medical journal (patient) has the following attributes:
	Name
	Social Security Number

An doctor has the following attributes:
	Name
	id
	Department

The API should support:
	Check if doctor X has access to patient Y medical journal
The API may support:
	Create new doctor
	Create new patient
	Get a list of all patients for a doctor
	Get a list of all doctors for a patient
	Assign a doctor to a patient

You don't need to consider authentication of a doctor. For the sake of this implementation, we can assume the identity of a doctor with a doctor query parameter

  

localhost:8080/getPatient?patientID=<CPR>&doctorID=<DOCTOR_WITH_ACCESS>

localhost:8080/getPatient?patientID=<CPR>&doctorID=<DOCTOR_WITHOUT_ACCESS>
  

A patient can't exist without a medical journal

It should not be possible for a doctor to see a medical journal from a patient that is not his and currently not in his department.


-----------------------------------------------------------------------------------------------------------------------------------

This challenge "solution" was written in python utilising flask for the web api, it is by no means finished as after 4 hours I ran into issues and decided to end it there. 
However the structure of and future plans are documented in the files. 
Beer in mind that it currently does not compile. 




