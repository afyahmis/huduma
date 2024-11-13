from datetime import datetime

from registry.domain.patient import Patient


def test_patient_init():
    patient = Patient("Johnny Doe", datetime(2001, 2, 2))
    assert patient.name == "Johnny Doe"
    assert patient.dob == datetime(2001, 2, 2)
