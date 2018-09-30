import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from app.utils.fetcher import Fetcher
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

    def up_scholarship(self, roll_number=32, standard=10, year=2006):
        with Spider() as spider:
            driver = spider.driver()
            driver.maximize_window()
            url = "http://164.100.181.105/scholarship/RegistrationNew.aspx"
            driver.get(url)

            links = {}
            links["obc"] = {}
            links["obc"]["postmatric"] = driver.find_element_by_css_selector(
                "#ctl00_ContentPlaceHolder1_lnbPostFreshOBC")

            links["obc"]["postmatric"].click()

            disctrict = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_district"))
            # disctrict_selected = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_district option:selected").text
            disctrict.select_by_visible_text("Muzaffarnagar")

            institute = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_institute"))
            institute.select_by_visible_text("SMT. MUKHTIYARI DEVI TIKAIT KANYA  MAHAVIDHYALAYA SISOULI")

            caste = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_caste"))
            caste.select_by_visible_text("अन्य पिछड़ा वर्ग (अल्पसंख़्यक पिछड़े वर्ग को छोड़कर)")

            religion = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_relegion"))
            religion.select_by_visible_text("Hindu")

            name_student = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_studentname")
            name_student.send_keys("Km Shalu")

            name_father = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_father_husbandname")
            name_father.send_keys("Swaraj Chaudhary")

            name_mother = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_mothername")
            name_mother.send_keys("Seeta Devi")

            d_o_b = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_dob")
            d_o_b.send_keys("03/01/1929")

            gender = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_gender"))
            gender.select_by_visible_text("FEMALE")

            highschool_year = Select(
                driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_highschpassyear"))
            highschool_year.select_by_visible_text("2008")

            board = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddl_board"))
            board.select_by_visible_text("UP BOARD")

            highschool_roll_no_a = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_hghrollnoA")
            # highschool_roll_no_a.send_keys("5239666") #Leave empty

            highschool_roll_no = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_hghrollno")
            highschool_roll_no.send_keys("5239666")

            school_name_address = driver.find_element_by_css_selector(
                "#ctl00_ContentPlaceHolder1_txt_schnameAdd_10class")
            school_name_address.send_keys("Kanya Pathshala Muzaffarnagar")

            mobile = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_mobileno")
            # mobile.send_keys("8546132642") #Leave empty

            phone = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_phoneno")
            # phone.send_keys("8546132642") #Leave empty

            email = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_emailid")
            email.send_keys("kukkaduku@gmail.com")

            password_value = "Xd@744"
            password = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_pwd")
            password.send_keys(password_value)

            password_confirm = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txt_pwd_confirm")
            password_confirm.send_keys(password_value)

            password_captcha = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txtCaptcha")
            # password_captcha.send_keys("") #TODO: Maybe?

            captcha = driver.find_element_by_css_selector("#Captcha").get_attribute("src")
            captcha_text = self.captcha(url=captcha)

            captcha_input = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_txtCaptcha")
            captcha_input.send_keys(captcha_text)

            submit = driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_btn_submit")
            # submit.click()

            registration_number = driver.find_element_by_css_selector("#txt_appid")
            print(registration_number.text)

            return "!"

    def captcha(self, url):
        """
        Ref: https://gist.github.com/chroman/5679049
        :return:
        """
        import cv2
        import pytesseract

        captcha_path = Fetcher().get_file_from_url(image_url=url)

        # flag = 1 | 2 | 4
        flag = 1

        # captcha_path = 'C:\\Dev\\Samanvaya\\src\\flask\\app\\utils\\captcha.jpg'
        # captcha_path = 'C:\\Dev\\Samanvaya\\src\\flask\\app\\utils\\whatsapp.png'
        # gray = cv2.imread(captcha_path, cv.IMREAD_GRAYSCALE)
        # cv2.threshold(gray, gray, 231, 255, cv.THRESH_BINARY)
        image = cv2.imread(captcha_path)
        cv2.imwrite("captcha1.png", image)
        # cv2.imshow("captcha", image)
        # cv2.waitKey(0)
        if flag & 1 == 1:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("captcha2.png", image)
            # cv2.imshow("captcha", gray)
            # cv2.waitKey(0)
        if flag & 2 == 2:
            image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)[1]
            cv2.imwrite("captcha3.png", image)
            # cv2.imshow("captcha", gray)
            # cv2.waitKey(0)
        if flag & 4 == 4:
            image = cv2.medianBlur(image, 3)
            cv2.imwrite("captcha4.png", image)
            # cv2.imshow("captcha", image)
            # cv2.waitKey(0)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, image)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        from PIL import Image
        image = Image.open(filename)
        text = pytesseract.image_to_string(image,
                                           config=
                                           '--psm 10'  # 8,9,10, 13
                                           # '--oem 3 '
                                           '-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz'
                                           # '-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz'
                                           )
        os.remove(filename)
        print(text)

        # api = tesseract.TessBaseAPI()
        # api.Init(".", "eng", tesseract.OEM_DEFAULT)
        # api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
        # api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
        # tesseract.SetCvImage(gray, api)
        # print(api.GetUTF8Text())
        return text
