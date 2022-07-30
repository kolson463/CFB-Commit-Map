import requests
from bs4 import BeautifulSoup
import json

commitArray =[]

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

python_jobs = results.find_all("class", string=lambda text: "python" in text.lower())

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#print(len(python_jobs))

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
         link_url = link["href"]
         #print(f"Apply here: {link_url}\n")


# job_elements = results.find_all("div", class_="card-content")


HUSKERURL ="https://www.on3.com/college/nebraska-cornhuskers/football/2023/commits/"

huskerPage = requests.get(HUSKERURL)

huskerSoup = BeautifulSoup(huskerPage.content, "html.parser")

huskerResults= huskerSoup.find(attrs={"class":"CommitList_commitListContainer__kZNC0"})

uls = huskerResults.find_all("div", class_="CommitListItem_playerWrapper__56t1h")


for ul in uls: 
    playerName = ul.find("a", class_="MuiTypography-root MuiLink-root MuiLink-underlineHover CommitListItem_name__2_3_6 MuiTypography-h5 MuiTypography-colorPrimary")        
    playerLocation = ul.find("p", class_="MuiTypography-root CommitListItem_hometownHighschool__BPAVm MuiTypography-body1 MuiTypography-colorTextPrimary")        
    # print(playerName.text.strip())
    # print(playerLocation.text.strip())
    commit = {"player":playerName.text.strip(),"location":playerLocation.text.strip()}
    commitArray.append(commit)

#print(commitArray)

for player in commitArray:
    print("Name: " + player["player"])
    print("Location: "+ player["location"])








