class Patient(object):
    patient_id = 0

    def __init__(self, name, allergies):
        Patient.patient_id += 1
        self.id = Patient.patient_id
        self.name = name
        self.allergies = allergies
        self.bedNumber = 0

    def setBedNumber(self, bedNumber):
        self.bedNumber = bedNumber

    def resetBedNumber(self):
        self.bedNumber = 0  # Just for that specific patient

    def display(self):
        print "===================="
        print "patient.id: {}".format(self.id)
        print "patient.name: {}".format(self.name)
        print "patient.allergies: {}".format(self.allergies)
        print "patient.bedNumber: {}".format(self.bedNumber)


class Hospital(object):
    bedNumber = 0

    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Sorry, our hopsital is full.  {} was denied entry".format(patient.name)
        else:
            print "Admission is complete for {}.".format(patient.name)
            # add patients to list of patients the square brackets [  ]
            self.patients.append(patient)
            Hospital.bedNumber += 1
            #patient.bedNumber = Hospital.bedNumber
            patient.setBedNumber(Hospital.bedNumber)

    def discharge(self, patient):
        patient.resetBedNumber()
        self.patients.remove(patient)
        print "{} has kicked out {}".format(self.name, patient.name)

    def display(self):
        for patient in self.patients:
            patient.display()


h1 = Hospital("HoppyHospital", 2)
p1 = Patient("BunnyCha", "sulfa based antibiotics")
p2 = Patient("GoldfishTrang", "Penicillin")
p3 = Patient("Lincoln", "Bullets")
# now, admit p1 into h1
h1.admit(p1)
h1.admit(p2)
h1.admit(p3)

h1.discharge(p1)

# p1.display()
# p2.display()
h1.display()

# print "Seeing bed number for {}".format(p1.name)
# p1.display()
