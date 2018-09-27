from selenium.webdriver.common.keys import Keys

from app.utils.spider import Spider


class Scrape():
    def __init__(self):
        pass

    def cbse(self, roll_number, standard=10, year=2006):
        with Spider() as spider:
            driver = spider.driver()
            url = "http://resultsarchives.nic.in/cbseresults/cbseresults{0}/class{1}/cbse{1}.htm".format(year, standard)
            driver.get(url)
            input = driver.find_element_by_tag_name("input")
            input.clear()
            input.send_keys(roll_number)
            input.send_keys(Keys.RETURN)

            result = {}
            columns = [column.text for column in
                       driver.find_elements_by_css_selector("body > div:nth-child(7) > table  tr  td  font")]

            result["roll_number"] = columns[1]
            assert result["roll_number"] == roll_number
            result["name"] = columns[4]
            result["mother_name"] = columns[6]
            result["father_name"] = columns[8]
            result["d_o_b"] = columns[10]

            result["subjects"] = []
            rows = driver.find_elements_by_css_selector("center table tr")
            for row in rows[1:-1]:
                columns = row.find_elements_by_css_selector("td font")
                subject = {}
                subject["code"] = columns[0].text
                subject["name"] = columns[1].text
                subject["marks"] = columns[2].text
                subject["grade"] = columns[3].text
                result["subjects"].append(subject)
            status_raw = rows[-1].find_element_by_css_selector("td font").text
            result["status"] = str(status_raw).split(":")[-1].strip()
            return result
