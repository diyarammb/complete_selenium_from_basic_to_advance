from Login import *
def ScrapeData(hw):
        Login()
        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        time.sleep(1)
        aElement=hw.GetElementlistofText("//a[@class='fd-link fd-link--compact']","xpath")
        for i in  aElement:
            link=hw.getElement(f"//a[.='{i}']","xpath")
            link.click()
            time.sleep(1)
            try:
                hw.getElement("//button[@name='OK']", "xpath").click()
                time.sleep(1)
            except:
                print("No OK Button")

            scaleDecription=hw.GetElementText("//span[@class='ratingScaleTextArea']","xpath")
            print(scaleDecription)
            score = hw.GetElementlistofattributeText(
                    "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
                    'xpath', 'value')
            label = hw.GetElementlistofattributeText(
                    "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
                    'xpath', 'value')
            desc = hw.GetElementlistofText(
                    "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
                    'xpath')

            for id, s in enumerate(score):
                    print(f"Score :{s} Lable : {label[id] } Descriptions : {desc[id]} \n\n")
            time.sleep(1)
            hw.getElement("//span[@class=' icon icon_cancel']","xpath").click()
            time.sleep(1)

ScrapeData(hw)