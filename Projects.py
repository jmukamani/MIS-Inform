import datetime

project_name = "Amahoro Stadium Refurbishment"
project_location = "Kigali City, Kigali Province"
project_description = "Renovating Amahoro stadium to align with international stadium standards. The objective is to make Kigali a sporting destination and promote tourism in Rwanda."
duration_months = 12
estimated_completion_date = datetime.date.today() + datetime.timedelta(days=duration_months*30)
project_status = "Ongoing"

print("Name:", project_name)
print("Location:", project_location)
print("Description:", project_description)
print("Estimated Completion Date:", estimated_completion_date.strftime("%d %B %Y"))
print("Status:", project_status)
