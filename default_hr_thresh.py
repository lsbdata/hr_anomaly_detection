def bpm_status (bpm, age_in_months):
	#Returns a heart rate alert if heart rate is outside of clinical bounds based on age. bpm and age in months are ints. A month is equal to 30.4 days or 4.3 weeks of age since dob.
	Abnormal_LOW_HR = 0
	Abnormal_HIGH_HR = 0
	if age_in_months <= 1 and bpm < 70:
		Abnormal_LOW_HR = 1
	elif age_in_months <= 1 and bpm > 190:
		Abnormal_HIGH_HR = 1
	elif 1 < age_in_months <= 3 and bpm < 100:
		Abnormal_LOW_HR = 1
	elif 1 < age_in_months <= 3 and bpm > 150:
		Abnormal_HIGH_HR = 1 	
	elif  3 < age_in_months <= 6 and bpm < 90:
		Abnormal_LOW_HR = 1
	elif  3 < age_in_months <= 6 and bpm > 120:
		Abnormal_HIGH_HR = 1	
	elif 6 < age_in_months <= 12 and bpm < 80:
		Abnormal_LOW_HR = 1
	elif 6 < age_in_months <= 12 and bpm > 120:
		Abnormal_HIGH_HR = 1	
	elif age_in_months > 12 and bpm < 70:
		Abnormal_LOW_HR = 1
	elif age_in_months > 12 and bpm > 110:
		Abnormal_HIGH_HR = 1
	return Abnormal_HIGH_HR, Abnormal_LOW_HR

bpm_status(200, 1)