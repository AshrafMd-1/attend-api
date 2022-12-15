from bs4 import BeautifulSoup
import pandas as pd
import regex as re


def scrap_attend(session):
    start_url = "https://samvidha.iare.ac.in/home?action=stud_att_STD"
    r = session.get(start_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    full_table = soup.select(
        "body > div > div.content-wrapper > section.content > div.card.card-info > div.card-body.dataTables_wrapper > "
        "table")[
        0]

    table_header = []
    for element in full_table.select("th"):
        element = re.sub(r'[^\x00-\x7F]+', ' ', element.text.strip())
        element = element.replace(" ", "_")
        table_header.append(element)

    table_data = []
    for element in full_table.select("tr")[1:-1]:
        row_data = []
        for value in element.select("td"):
            value = re.sub(r'[^\x00-\x7F]+', ' ', value.text.strip())
            value = value.replace(" ", "_")
            row_data.append(value)
        table_data.append(row_data)

    df = pd.DataFrame(table_data, columns=table_header)
    return df
