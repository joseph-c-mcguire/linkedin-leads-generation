import csv
import requests


def fetch_linkedin_profiles():
    # Use LinkedIn API or Selenium approach
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    response = requests.get(
        "https://api.linkedin.com/v2/peopleSearch?q=people&keywords=Data%20Scientist",
        headers=headers,
    )
    process_response_data(response)


def process_response_data(response):
    data = response.json()

    write_profiles_to_csv(data)


def write_profiles_to_csv(data):
    with open("output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Contact", "Headline"])

        for person in data["elements"]:
            write_person_data(writer, person)


def write_person_data(writer, person):
    name = person["firstName"] + " " + person["lastName"]
    contact = "N/A"  # Replace with real contact if available
    headline = person.get("headline", "")
    writer.writerow([name, contact, headline])
