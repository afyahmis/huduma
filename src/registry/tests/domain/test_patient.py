from datetime import datetime

from domain.patient import Patient


def test_patient_init():
    patient = Patient(1,"John Doe",datetime(2000,1,1))
    assert patient.id == 1
    assert patient.name == "John Doe"
    assert patient.dob == datetime(2000,1,1)
