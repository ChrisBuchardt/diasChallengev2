
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
#Initial Python Script
def Basic():
	return "Hey this is just a placeholder blank page. /n go to get getPatient"

#I am not the greatest fan of using the DOCTOR_WITH_ACCESS so lets just use an ID. 
@app.route("/getPatient?patientID=<CPR>&doctorID=<DOCTORID>", methods=['GET'])
def returnPatient(patientID, doctorID):

	if checkAccess(patientID, doctorID):
		return findPatient(patientID)
	else return "Invalid ID"


@app.route("/getDoctor/<doctorID>", methods=['GET'])
def returnDoctor(doctorID):
	return findDoctor(doctorID)


#This one is a bit rough with my current implementation, for now do not route it
#@app.route("/addAdmission", methods=['POST'])
def addAdmission(Department, Doctors, Journal):
	createAdmission(Department, Doctors, Journal)
	return "Admission added"

#--------------------------------Classes ----------------------------------------------------

#Thoughs behind doctor class
#We keep it simple, we have a string name, an int id and a string department
class Doctor:
	name = "default"
	dID = 0
	department = "none"

	def __init__(self, n, i, dep):
		self.name = n
		self.dID = i
		self.department = dep

#Keep the patient simple, we should avoid sharing to much information about the patient so we can only access it by the admissions
class Patient:
	name = "default"
	SSN = "000000-0000"

	def __init__(self, n, s):
		self.name=n
		self.SSN=s


#The connective tissue between the doctor and patients
class Admission:
	departments = "none"
	doctors = []
	patient = "0"


	#We require a department, list of doctors and journal
	def __init__(self, dep, do, journ):
		self.department = dep
		self.doctors = do
		self.patient=s


#Was gonna use an enum but for now we can just use strings. 
#TODO consider makign departments thier own document which utilises enums
#class department(Enum):
#    UNASSIGNED = 1
#    ADMISSIONS = 2
#    ANESTHETICS = 3
#    BURNWARD = 4
#    CARDIOLOGY = 5
#    CRITIALCARE = 6 
#    GASTROENTEROLOGY = 7
#    ICU = 8
#    PEDIATRIC = 9
#    ER = 10


#---------------------------------Non-@app.routed code-----------------------------------------

#For now I keep this as one single script. 
#We seperate the two types of functions as this is more internal scrips 


#We keep it simple, as we only got a couple of hours
patients = []
doctors = []
admissions = []

#We define 3 simple create functions, utilising the contructures from their respective classes
def createDoctor(name, i, dep):
	d = Doctor(name,i,dep)

	if d not in doctors:
		doctors.append(d)

def createPatient(name, nr):
	p = Patient(name,nr)

	if p not in patients:
		patients.append(p)

#Bear in mind that admission does not check if the doctors exist. 
def createAdmission(dep, doc, jour):
	a = Admission(dep, doc, jour)

	if a not in admissions:
		admissions.append(a)


#Function for searching admissions for patient id's returning the relevant admission. 
def findAdmission(patientID):

	for a in admissions:
		if a.patient.SSN == patientID:
			return a
	#If we do not return a, we return null/None
	return None

#Function to return doctor object from the list of all Doctors.
def findDoctor(doctorID):

	for d in doctors:
		if d.dID==doctorID:
			return d
	
	return None

#Function to return the patient object from the list of All patients
def findPatient(patientID)

	for p in patients:
		if p.SSN == patientID:
			return p

	return None


#Function for checking access for doctor and patient.
#Fulfilles the "Check if doctor X has access to patient Y medical journal" should have
def checkAccess(patientID, doctorID):
	#We first find the admission
	a = findAdmission(patientID)
	if a==None:
		return False
	else:
		#Then we find the doctor
		d = findDoctor(doctorID)
		if d==None:
			return False
		else:
			#Then we return the comparison between the departments
			return a.department==d.department


		#Initially i though we wanted to find the doctor who made the admission
		#But we just need to check department
		#for i in a.doctors:
		#	if i.dID==doctorID:
		#		return True


#Function to get a new list of patients for a single doctor
#Fulfilles the "Get a list of all patients for a doctor" could have
def getAllJournalsForDoctor(doctorID):
	journals = []

	for p in patients:
		if checkAccess(p.SSN, doctorID):
			journals.append(p)



#Function to get a new list of doctors for a single patient 
#Fulfilles the "Get a list of all doctors for a patient" could have
def getAllDoctorsForJournal(patientID)
	docs = []

	for d in doctors:
		if checkAccess(patientID, d.dID):
			docs.append(d)
